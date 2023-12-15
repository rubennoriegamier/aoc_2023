import fileinput
import re
from functools import cache
from itertools import repeat


def main():
    rows = list(map(parse_row, fileinput.input()))

    print(part_1(rows))
    print(part_2(rows))


POINTS_RE = re.compile(r'\.+')


def parse_row(raw_row: str) -> tuple[str, tuple[int, ...]]:
    format_a, raw_format_b = raw_row.split()

    return format_a, tuple(map(int, raw_format_b.split(',')))


def compress(format_a: str) -> str:
    return '.'.join(POINTS_RE.split(format_a.strip('.')))


@cache
def arrangements(format_a: str, format_b: tuple[int, ...]) -> int:
    if not format_b:
        return int('#' not in format_a)

    if len(format_a) < format_b[0] or len(format_a) - format_a.count('.') < sum(format_b):
        return 0

    match format_a[0]:
        case '#':
            if len(format_a) == format_b[0]:
                return int(len(format_b) == 1 and '.' not in format_a)

            if '.' in format_a[:format_b[0]] or format_a[format_b[0]] == '#':
                return 0

            return arrangements(format_a[format_b[0] + 1:].lstrip('.'), format_b[1:])
        case '?':
            return (arrangements(format_a[1:].lstrip('.'), format_b) +
                    arrangements('#' + format_a[1:], format_b))
        case _:
            raise NotImplementedError


def part_1(rows: list[tuple[str, tuple[int, ...]]]) -> int:
    return sum(arrangements(compress(format_a), format_b)
               for format_a, format_b in rows)


def part_2(rows: list[tuple[str, tuple[int, ...]]]) -> int:
    return sum(arrangements(compress('?'.join(repeat(format_a, 5))), format_b * 5)
               for format_a, format_b in rows)


if __name__ == '__main__':
    main()
