from day07 import sort_hands
from hand import Hand


def solve(puzzle_input: list[str]) -> int:
    result = 0
    bids: dict[Hand, int] = {}
    for line in puzzle_input:
        cards, bid = line.split()
        bids[Hand(cards)] = int(bid)
    hands_by_strength = sort_hands(list(bids.keys()))
    amount_hands = len(bids)
    for hand, rank in zip(hands_by_strength, range(amount_hands, 0, -1)):
        result += bids[hand] * rank
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
