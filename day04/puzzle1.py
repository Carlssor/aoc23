import day04


def solve(puzzle_input: list[str]) -> int:
    result = 0
    for line in puzzle_input:
        played_numbers, winning_numbers = day04.get_played_and_winning_numbers(line)
        result += day04.calculate_score(played_numbers, winning_numbers)
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
