import day04


def solve(puzzle_input: list[str]) -> int:
    amount_copies: list[int] = [1] * len(puzzle_input)
    for game_index, line in enumerate(puzzle_input):
        played_numbers, winning_numbers = day04.get_played_and_winning_numbers(line)
        amount_winning_numbers = day04.calculate_correct_played_numbers(played_numbers, winning_numbers)
        for bonus_card_index in range(game_index + 1, game_index + amount_winning_numbers + 1):
            amount_copies[bonus_card_index] += amount_copies[game_index]
    return sum(amount_copies)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
