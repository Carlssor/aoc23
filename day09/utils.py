def get_history(line: str) -> list[int]:
    return [int(val) for val in line.split()]


def get_differences(history: list[int]) -> list[int]:
    return [history[index] - history[index - 1] for index in range(1, len(history))]