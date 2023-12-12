from utils import get_history, get_differences


def solve(puzzle_input: list[str]) -> int:
    result = 0
    for line in puzzle_input:
        dataset = [get_history(line)]
        while any(dataset[-1]):
            dataset.append(get_differences(dataset[-1]))
        dataset[-1].insert(0, 0)
        for index in range(len(dataset) - 1, 0, -1):
            value_to_subtract = dataset[index][0]
            previous_first_value = dataset[index - 1][0]
            dataset[index - 1].insert(0, previous_first_value - value_to_subtract)
        result += dataset[0][0]
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
