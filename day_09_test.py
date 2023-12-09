from unittest import TestCase, main

from day_09 import parse_history, next_value, part_1, part_2


class TestDay09(TestCase):
    _histories: list[list[int]]

    def setUp(self):
        self._histories = list(map(parse_history, ['0 3 6 9 12 15',
                                                   '1 3 6 10 15 21',
                                                   '10 13 16 21 30 45']))

    def test_next_value(self):
        for history, next_value_ in zip(self._histories, [18, 28, 68]):
            with self.subTest(item_type=history):
                self.assertEqual(next_value(history), next_value_)

    def test_part_1(self):
        self.assertEqual(part_1(self._histories), 114)

    def test_part_2(self):
        self.assertEqual(part_2(self._histories), 2)


if __name__ == '__main__':
    main()
