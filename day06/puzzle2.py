import day06


def parse_time_and_distance(puzzle_input: list[str]) -> tuple[int, int]:
    time_allowed = int(puzzle_input[0].split(maxsplit=1)[1].replace(" ", ""))
    distance = int(puzzle_input[1].split(maxsplit=1)[1].replace(" ", ""))
    return time_allowed, distance


def solve(puzzle_input: list[str]) -> int:
    time_allowed, distance = parse_time_and_distance(puzzle_input)
    for hold_time in range(time_allowed):
        if day06.calculate_distance_travelled(hold_time, time_allowed) > distance:
            amount_holding_times_to_win = time_allowed - 2 * hold_time + 1
            return amount_holding_times_to_win


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
