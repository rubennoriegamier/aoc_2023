import fileinput
from itertools import pairwise


def main():
    histories = list(map(parse_history, fileinput.input()))

    print(part_1(histories))
    print(part_2(histories))


def parse_history(raw_history: str) -> list[int]:
    return list(map(int, raw_history.split()))


def next_value(history: list[int]) -> int:
    values = []

    while any(history):
        values.append(history[-1])
        history = [b - a for a, b in pairwise(history)]

    return sum(values)


def part_1(histories: list[list[int]]) -> int:
    return sum(map(next_value, histories))


def part_2(histories: list[list[int]]) -> int:
    return sum(map(next_value, (history[::-1] for history in histories)))


if __name__ == '__main__':
    main()
