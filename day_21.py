import fileinput
from operator import sub


def main():
    garden = Garden(list(map(str.rstrip, fileinput.input())))

    print(garden.part_1(64))
    print(garden.part_2())


class Garden:
    _garden: list[list[bool]]
    _start: tuple[int, int]

    def __init__(self, garden: list[str]):
        self._garden = []

        for y, row in enumerate(garden):
            self._garden.append([])

            for x, tile in enumerate(row):
                match tile:
                    case '#':
                        self._garden[-1].append(False)
                    case '.':
                        self._garden[-1].append(True)
                    case 'S':
                        self._garden[-1].append(True)
                        self._start = y, x

    def part_1(self, steps: int) -> int:
        plots = {self._start}

        h = len(self._garden)
        w = len(self._garden[0])

        for _ in range(steps):
            next_plots = set()

            for y, x in plots:
                if y > 0 and self._garden[y - 1][x]:
                    next_plots.add((y - 1, x))
                if y < h - 1 and self._garden[y + 1][x]:
                    next_plots.add((y + 1, x))
                if x > 0 and self._garden[y][x - 1]:
                    next_plots.add((y, x - 1))
                if x < w - 1 and self._garden[y][x + 1]:
                    next_plots.add((y, x + 1))

            plots = next_plots

        return len(plots)

    def part_2(self) -> int:
        plots = {self._start}

        h = len(self._garden)
        w = len(self._garden[0])

        first_steps = []

        for n in range(1, 26_501_365 + 1):
            next_plots = set()

            for y, x in plots:
                if self._garden[(y - 1) % h][x % w]:
                    next_plots.add((y - 1, x))
                if self._garden[(y + 1) % h][x % w]:
                    next_plots.add((y + 1, x))
                if self._garden[y % h][(x - 1) % w]:
                    next_plots.add((y, x - 1))
                if self._garden[y % h][(x + 1) % w]:
                    next_plots.add((y, x + 1))

            plots = next_plots

            if (n - h // 2) % h == 0:
                first_steps.append(len(plots))
                if len(first_steps) == 3:
                    diffs_a = list(map(sub, first_steps[1:], first_steps))
                    diff_b = diffs_a[1] - diffs_a[0]
                    rem_cycles = (26_501_365 - n) // h

                    return first_steps[-1] + \
                        diffs_a[-1] * rem_cycles + \
                        diff_b * sum(range(1, rem_cycles + 1))

        return len(plots)


def empty_serie():
    n = 1
    i = 1

    while True:
        yield n

        i += 2
        n += i


if __name__ == '__main__':
    main()
