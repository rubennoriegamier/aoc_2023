import unittest
from operator import itemgetter

from day_07 import parse_hand_and_bid, hand_type, hand_type_with_jokers, part_1, part_2


class TestDay07(unittest.TestCase):
    _hands_and_bids: list[tuple[tuple[int, int, int, int, int], int]]

    def setUp(self):
        self._hands_and_bids = list(map(parse_hand_and_bid, ['32T3K 765',
                                                             'T55J5 684',
                                                             'KK677 28',
                                                             'KTJJT 220',
                                                             'QQQJA 483']))

    def test_hand_type(self):
        for hand, type_ in zip(map(itemgetter(0), self._hands_and_bids), [2, 4, 3, 3, 4]):
            with self.subTest(item_type=hand):
                self.assertEqual(hand_type(hand), type_)

    def test_hand_type_with_jokers(self):
        for hand, type_ in zip(map(itemgetter(0), self._hands_and_bids), [2, 6, 3, 6, 6]):
            with self.subTest(item_type=hand):
                hand = tuple(1 if card == 11 else card for card in hand)
                # noinspection PyTypeChecker
                self.assertEqual(hand_type_with_jokers(hand), type_)

    def test_part_1(self):
        self.assertEqual(part_1(self._hands_and_bids), 6_440)

    def test_part_2(self):
        self.assertEqual(part_2(self._hands_and_bids), 5_905)


if __name__ == '__main__':
    unittest.main()
