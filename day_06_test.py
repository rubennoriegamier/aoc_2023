import unittest

from day_06 import part_1, part_2, wins


class TestDay06(unittest.TestCase):
    _sheet: list[tuple[int, int]]

    def setUp(self):
        self._sheet = [(7, 9),
                       (15, 40),
                       (30, 200)]

    def test_wins(self):
        for (time, record), wins_ in zip(self._sheet, [4, 8, 9]):
            with self.subTest(item_type=(time, record)):
                self.assertEqual(wins(time, record), wins_)

    def test_part_1(self):
        self.assertEqual(part_1(self._sheet), 288)

    def test_part_2(self):
        self.assertEqual(part_2(self._sheet), 71_503)


if __name__ == '__main__':
    unittest.main()
