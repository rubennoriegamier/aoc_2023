import itertools as it
from functools import reduce
from math import ceil, floor
from operator import mul


def main():
    times: list[int] = list(map(int, input().split(':')[1].split()))
    records: list[int] = list(map(int, input().split(':')[1].split()))
    sheet: list[tuple[int, int]] = list(zip(times, records))

    print(part_1(sheet))
    print(part_2(sheet))


def part_1(sheet: list[tuple[int, int]]) -> int:
    return reduce(mul, it.starmap(wins, sheet))


def solve_quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    sqrt = (b ** 2 - 4 * a * c) ** 0.5

    return (-b + sqrt) / (2 * a), (-b - sqrt) / (2 * a)


def wins(time: int, record: int) -> int:
    a, b = solve_quadratic(-1, time, -record - 1)

    return floor(b) - ceil(a) + 1


def part_2(sheet: list[tuple[int, int]]) -> int:
    times, records = zip(*sheet)
    time_ = int(''.join(map(str, times)))
    record = int(''.join(map(str, records)))

    return wins(time_, record)


if __name__ == '__main__':
    main()
