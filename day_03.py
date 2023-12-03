import fileinput
import re
from collections import defaultdict
from operator import methodcaller, mul
from typing import Final


def main():
    eng: list[str] = list(map(str.rstrip, fileinput.input()))

    print(part_1(eng))
    print(part_2(eng))


NUM_RE: Final = re.compile(r'\d+')


def part_1(eng: list[str]) -> int:
    return sum(int(line[x_from:x_to])
               for y, line in enumerate(eng)
               for x_from, x_to in map(methodcaller('span'), NUM_RE.finditer(line))
               if any(any(c != '.' and not '0' <= c <= '9'
                          for c in line_[max(x_from - 1, 0):x_to + 1])
                      for line_ in eng[max(y - 1, 0):y + 2]))


def part_2(eng: list[str]) -> int:
    gears: defaultdict[tuple[int, int], list[int]] = defaultdict(list)

    for y, line in enumerate(eng):
        for x_from, x_to in map(methodcaller('span'), NUM_RE.finditer(line)):
            if gear := next(((y_, x_)
                             for y_ in range(max(y - 1, 0), min(y + 2, len(eng)))
                             for x_ in range(max(x_from - 1, 0), min(x_to + 1, len(line)))
                             if eng[y_][x_] == '*'), None):
                gears[gear].append(int(line[x_from:x_to]))

    return sum(mul(*nums) for nums in gears.values() if len(nums) == 2)


if __name__ == '__main__':
    main()
