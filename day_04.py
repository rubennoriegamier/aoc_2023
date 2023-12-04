import fileinput
from functools import cache, partial
from operator import add, and_, lshift


def main():
    cards: list[int] = list(map(parse_card, fileinput.input()))

    print(part_1(cards))
    print(part_2(cards))


def parse_card(raw_card: str) -> int:
    return len(and_(*map(set, map(str.split, raw_card.split(': ')[1].split(' | ')))))


def part_1(cards: list[int]) -> int:
    return sum(map(partial(lshift, 1),
                   map(partial(add, -1),
                       filter(None, cards))))


def part_2(cards: list[int]) -> int:
    @cache
    def count(i: int) -> int:
        return 1 + sum(map(count, range(i + 1, min(i + 1 + cards[i], len(cards)))))

    return sum(map(count, range(len(cards))))


if __name__ == '__main__':
    main()
