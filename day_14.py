import fileinput


def main():
    platform = list(map(str.rstrip, fileinput.input()))

    print(part_1(platform))
    print(part_2(platform))


def part_1(platform: list[str]) -> int:
    free = [0] * len(platform[0])
    load = 0

    for y, row in enumerate(platform):
        for x, tile in enumerate(row):
            match tile:
                case '.':
                    free[x] += 1
                case '#':
                    free[x] = 0
                case 'O':
                    load += len(platform) - y + free[x]
                case _:
                    raise NotImplementedError

    return load


def part_2(platform: list[str]) -> int:
    # noinspection PyTypeChecker
    platform = list(map(list, platform))

    loads = []

    for _ in range(1_000_000_000):
        # North
        free = [0] * len(platform[0])

        for y in range(len(platform)):
            for x in range(len(platform[0])):
                match platform[y][x]:
                    case '.':
                        free[x] += 1
                    case '#':
                        free[x] = 0
                    case 'O':
                        if free[x]:
                            platform[y - free[x]][x] = 'O'
                            platform[y][x] = '.'
                    case _:
                        raise NotImplementedError

        # West
        free = [0] * len(platform)

        for x in range(len(platform[0])):
            for y in range(len(platform)):
                match platform[y][x]:
                    case '.':
                        free[y] += 1
                    case '#':
                        free[y] = 0
                    case 'O':
                        if free[y]:
                            platform[y][x - free[y]] = 'O'
                            platform[y][x] = '.'
                    case _:
                        raise NotImplementedError

        # South
        free = [0] * len(platform[0])

        for y in range(len(platform) - 1, -1, -1):
            for x in range(len(platform[0])):
                match platform[y][x]:
                    case '.':
                        free[x] += 1
                    case '#':
                        free[x] = 0
                    case 'O':
                        if free[x]:
                            platform[y + free[x]][x] = 'O'
                            platform[y][x] = '.'
                    case _:
                        raise NotImplementedError

        # East
        free = [0] * len(platform)
        loads.append(0)

        for x in range(len(platform[0]) - 1, -1, -1):
            for y in range(len(platform)):
                match platform[y][x]:
                    case '.':
                        free[y] += 1
                    case '#':
                        free[y] = 0
                    case 'O':
                        if free[y]:
                            platform[y][x + free[y]] = 'O'
                            platform[y][x] = '.'
                        loads[-1] += len(platform) - y
                    case _:
                        raise NotImplementedError

        if len(loads) >= 14 and loads[-7:] == loads[-14:-7]:
            return loads[-7:][(999_999_999 - len(loads)) % 7]


if __name__ == '__main__':
    main()
