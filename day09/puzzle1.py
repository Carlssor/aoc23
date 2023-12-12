from utils import get_history, get_differences


def solve(puzzle_input: list[str]) -> int:
    result = 0
    for line in puzzle_input:
        dataset = [get_history(line)]
        while any(dataset[-1]):
            dataset.append(get_differences(dataset[-1]))
        dataset[-1].append(0)
        for index in range(len(dataset) - 1, 0, -1):
            value_to_add = dataset[index][-1]
            previous_last_value = dataset[index - 1][-1]
            dataset[index - 1].append(previous_last_value + value_to_add)
        result += dataset[0][-1]
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
