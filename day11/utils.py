def find_galaxy_positions(image: list[str]) -> list[tuple[int, int]]:
    galaxy_positions = []
    for row, line in enumerate(image):
        col = -1
        while (col := line.find("#", col + 1)) != -1:
            galaxy_positions.append((row, col))
    return galaxy_positions
