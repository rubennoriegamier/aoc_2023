import fileinput
import itertools as it
from collections import Counter
from operator import itemgetter, mul


def main():
    hands_and_bids = list(map(parse_hand_and_bid, fileinput.input()))

    print(part_1(hands_and_bids))
    print(part_2(hands_and_bids))


def part_1(hands_and_bids: list[tuple[tuple[int, int, int, int, int], int]]) -> int:
    return sum(it.starmap(mul,
                          enumerate(map(itemgetter(1),
                                        sorted(hands_and_bids,
                                               key=lambda hb: (hand_type(hb[0]), hb[0]))), 1)))


def part_2(hands_and_bids: list[tuple[tuple[int, int, int, int, int], int]]) -> int:
    hands_and_bids = [(tuple(1 if card == 11 else card for card in hand), bid)
                      for hand, bid in hands_and_bids]

    return sum(it.starmap(mul,
                          enumerate(map(itemgetter(1),
                                        sorted(hands_and_bids,
                                               key=lambda hb: (hand_type_with_jokers(hb[0]), hb[0]))), 1)))


def parse_hand_and_bid(raw_hand_and_bid: str) -> tuple[tuple[int, int, int, int, int], int]:
    raw_hand, raw_bid = raw_hand_and_bid.split()

    # noinspection PyTypeChecker
    return tuple(map(card_strength, raw_hand)), int(raw_bid)


def card_strength(card: str) -> int:
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case 'T':
            return 10
        case _:
            return int(card)


def hand_type(hand: tuple[int, int, int, int, int]) -> int:
    top = Counter(hand).most_common()

    match (len(top), top[0][1]):
        # Five of a kind
        case (1, 5):
            return 7
        # Four of a kind
        case (2, 4):
            return 6
        # Full house
        case (2, 3):
            return 5
        # Three of a kind
        case (3, 3):
            return 4
        # Two pair
        case (3, 2):
            return 3
        # One pair
        case (4, 2):
            return 2
        # High card
        case _:
            return 1


def hand_type_with_jokers(hand: tuple[int, int, int, int, int]) -> int:
    if 1 not in hand:
        return hand_type(hand)

    counts = Counter(hand)
    top = counts.most_common()

    match (len(counts), counts[1], top[0][1]):
        case (1, _, _) | (2, _, _):
            return 7
        case (3, 1, 3) | (3, 2, 2) | (3, 3, 3):
            return 6
        case (3, 1, 2):
            return 5
        case (4, _, _):
            return 4
        case _:
            return 2


if __name__ == '__main__':
    main()
