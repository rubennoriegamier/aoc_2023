import fileinput
from functools import cached_property
from itertools import pairwise


def main():
    area = Area(list(map(str.rstrip, fileinput.input())))

    print(area.part_1())
    print(area.part_2())


class Area:
    _area: list[str]

    def __init__(self, area: list[str]):
        self._area = [f'.{row}.' for row in area]
        self._area.insert(0, '.' * len(self._area[0]))
        self._area.append(self._area[0])

    @cached_property
    def _start_yx(self) -> tuple[int, int]:
        return next((y, x)
                    for y, row in enumerate(self._area)
                    for x, tile in enumerate(row)
                    if tile == 'S')

    @cached_property
    def _start_pipe(self) -> str:
        y, x = self._start_yx

        if self._area[y - 1][x] in '|7F':
            if self._area[y + 1][x] in '|LJ':
                return '|'
            if self._area[y][x - 1] in '-LF':
                return 'J'
            else:
                return 'L'
        elif self._area[y + 1][x] in '|LJ':
            if self._area[y][x - 1] in '-LF':
                return '7'
            else:
                return 'F'
        else:
            return '-'

    @cached_property
    def _path(self) -> set[tuple[int, int]]:
        path = {self._start_yx}

        prev_y, prev_x = self._start_yx
        match self._start_pipe:
            case '|' | '7' | 'F':
                curr_y = prev_y + 1
                curr_x = prev_x
            case '-' | 'L':
                curr_y = prev_y
                curr_x = prev_x + 1
            case 'J':
                curr_y = prev_y
                curr_x = prev_x - 1
            case _:
                raise NotImplemented

        while (curr_y, curr_x) != self._start_yx:
            path.add((curr_y, curr_x))
            match self._area[curr_y][curr_x]:
                case '|':
                    prev_y, curr_y = curr_y, curr_y * 2 - prev_y
                case '-':
                    prev_x, curr_x = curr_x, curr_x * 2 - prev_x
                case 'L' | '7':
                    prev_y, curr_y, prev_x, curr_x = (curr_y, curr_y + curr_x - prev_x,
                                                      curr_x, curr_x + curr_y - prev_y)
                case 'J' | 'F':
                    prev_y, curr_y, prev_x, curr_x = (curr_y, curr_y + prev_x - curr_x,
                                                      curr_x, curr_x + prev_y - curr_y)

        return path

    def part_1(self) -> int:
        return len(self._path) >> 1

    def part_2(self) -> int:
        area = self._area.copy()
        area[self._start_yx[0]] = area[self._start_yx[0]].replace('S', self._start_pipe)

        return sum(len(''.join(area[y_from][x_] for x_ in range(x + 1, len(area[0]) - 1)
                               if area[y_from][x_] != '-' and (y_from, x_) in self._path)
                       .replace('L7', '|')
                       .replace('FJ', '|')) & 1
                   for (y_from, x_from), (y_to, x_to) in pairwise(sorted(self._path))
                   if y_from == y_to
                   for x in range(x_from + 1, x_to))


if __name__ == '__main__':
    main()
