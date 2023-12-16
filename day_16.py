import fileinput
from collections import defaultdict


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str], start=(0, 0, '>')) -> int:
    beams = defaultdict(set)
    heads = {start}

    while heads:
        y, x, direction = heads.pop()

        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and direction not in beams[y, x]:
            beams[y, x].add(direction)

            match direction:
                case '>':
                    match grid[y][x]:
                        case '/':
                            heads.add((y - 1, x, '^'))
                        case '\\':
                            heads.add((y + 1, x, 'v'))
                        case '|':
                            heads.add((y - 1, x, '^'))
                            heads.add((y + 1, x, 'v'))
                        case _:
                            heads.add((y, x + 1, '>'))
                case 'v':
                    match grid[y][x]:
                        case '/':
                            heads.add((y, x - 1, '<'))
                        case '\\':
                            heads.add((y, x + 1, '>'))
                        case '-':
                            heads.add((y, x - 1, '<'))
                            heads.add((y, x + 1, '>'))
                        case _:
                            heads.add((y + 1, x, 'v'))
                case '<':
                    match grid[y][x]:
                        case '/':
                            heads.add((y + 1, x, 'v'))
                        case '\\':
                            heads.add((y - 1, x, '^'))
                        case '|':
                            heads.add((y + 1, x, 'v'))
                            heads.add((y - 1, x, '^'))
                        case _:
                            heads.add((y, x - 1, '<'))
                case '^':
                    match grid[y][x]:
                        case '/':
                            heads.add((y, x + 1, '>'))
                        case '\\':
                            heads.add((y, x - 1, '<'))
                        case '-':
                            heads.add((y, x + 1, '>'))
                            heads.add((y, x - 1, '<'))
                        case _:
                            heads.add((y - 1, x, '^'))
                case _:
                    raise NotImplementedError

    return len(beams)


def part_2(grid: list[str]) -> int:
    return max(max(part_1(grid, (y, 0, '>')) for y in range(len(grid))),
               max(part_1(grid, (0, x, 'v')) for x in range(len(grid[0]))),
               max(part_1(grid, (y, len(grid[0]) - 1, '<')) for y in range(len(grid))),
               max(part_1(grid, (len(grid) - 1, x, '^')) for x in range(len(grid[0]))))


if __name__ == '__main__':
    main()
