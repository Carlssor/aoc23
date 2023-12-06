import day06


def parse_time_and_distance(puzzle_input: list[str]) -> list[tuple[int, int]]:
    times = [int(val) for val in puzzle_input[0].split()[1:]]
    distances = [int(val) for val in puzzle_input[1].split()[1:]]
    return list(zip(times, distances))


def solve(puzzle_input: list[str]) -> int:
    result = 1
    for time_allowed, distance in parse_time_and_distance(puzzle_input):
        for hold_time in range(time_allowed):
            if day06.calculate_distance_travelled(hold_time, time_allowed) > distance:
                amount_holding_times_to_win = time_allowed - 2 * hold_time + 1
                result *= amount_holding_times_to_win
                break
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
