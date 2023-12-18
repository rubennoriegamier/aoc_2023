import fileinput
from itertools import chain, pairwise, starmap
from typing import NamedTuple


def main():
    dig_plan = list(map(Dig.parse, fileinput.input()))

    print(part_1(dig_plan))
    print(part_2(dig_plan))


class Dig(NamedTuple):
    direction: str
    move: int
    color: str | None

    @classmethod
    def parse(cls, raw_dig: str) -> 'Dig':
        direction, raw_move, raw_color = raw_dig.split()

        return cls(direction, int(raw_move), raw_color[2:-1])

    def color_dig(self) -> 'Dig':
        move = int(self.color[:-1], 16)

        match self.color[-1]:
            case '0':
                direction = 'R'
            case '1':
                direction = 'D'
            case '2':
                direction = 'L'
            case '3':
                direction = 'U'
            case _:
                raise NotImplementedError

        return Dig(direction, move, None)


def part_1(dig_plan: list[Dig]) -> int:
    trench = []
    y = 0
    x = 0
    min_y = 0
    max_y = 0
    min_x = 0
    max_x = 0

    for dig in dig_plan:
        match dig.direction:
            case 'U':
                trench.append(((y - 1, x), (y - dig.move, x)))
                y -= dig.move
                min_y = min(min_y, y)
            case 'D':
                trench.append(((y + 1, x), (y + dig.move, x)))
                y += dig.move
                max_y = max(max_y, y)
            case 'L':
                trench.append(((y, x - 1), (y, x - dig.move)))
                x -= dig.move
                min_x = min(min_x, x)
            case 'R':
                trench.append(((y, x + 1), (y, x + dig.move)))
                x += dig.move
                max_x = max(max_x, x)
            case _:
                raise NotImplementedError

    for i, (((y_1_from, x_1_from), (y_1_to, x_1_to)),
            ((y_2_from, x_2_from), (y_2_to, x_2_to))) in enumerate(pairwise(chain(trench, [trench[0]]))):
        if y_1_from == y_1_to:
            (y_0_from, x_0_from), (y_0_to, x_0_to) = trench[i - 1]
            if x_1_from < x_1_to:
                if y_0_to < y_0_from and y_2_to < y_2_from:
                    #   ^          ^
                    # ^>>   ->   >>>
                    # ^          ^
                    trench[i] = (y_1_from, x_1_from - 1), (y_1_to, x_1_to)
                    trench[i - 1] = (y_0_from, x_0_from), (y_0_to + 1, x_0_to)
                elif y_0_to > y_0_from and y_2_to > y_2_from:
                    # v          v
                    # v>>   ->   >>>
                    #   v          v
                    trench[i] = (y_1_from, x_1_from - 1), (y_1_to, x_1_to)
                    trench[i - 1] = (y_0_from, x_0_from), (y_0_to - 1, x_0_to)
            else:
                if y_0_to < y_0_from and y_2_to < y_2_from:
                    # ^          ^
                    # <<^   ->   <<<
                    #   ^          ^
                    trench[i] = (y_1_from, x_1_from + 1), (y_1_to, x_1_to)
                    trench[i - 1] = (y_0_from, x_0_from), (y_0_to + 1, x_0_to)
                elif y_0_to > y_0_from and y_2_to > y_2_from:
                    #   v          v
                    # <<v   ->   <<<
                    # v          v
                    trench[i] = (y_1_from, x_1_from + 1), (y_1_to, x_1_to)
                    trench[i - 1] = (y_0_from, x_0_from), (y_0_to - 1, x_0_to)

    size = 0
    trench = list(map(tuple, map(sorted, trench)))
    ys = sorted(set(chain.from_iterable((y_from, y_to + 1)
                                        for (y_from, _), (y_to, _) in trench)))

    for y_range in starmap(range, pairwise(ys)):
        xs = sorted((x_from, x_to)
                    for (y_from, x_from), (y_to, x_to) in trench
                    if y_from <= y_range.start <= y_to)

        for i, ((x_1_from, _), (_, x_2_to)) in enumerate(pairwise(xs)):
            if i % 2 == 0:
                size += (x_2_to - x_1_from + 1) * len(y_range)

    return size


def part_2(dig_plan: list[Dig]) -> int:
    return part_1([dig.color_dig() for dig in dig_plan])


if __name__ == '__main__':
    main()
