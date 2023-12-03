import unittest

from day_03 import part_1, part_2


class TestDay03(unittest.TestCase):
    _eng: list[str]

    def setUp(self):
        self._eng = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']

    def test_part_1(self):
        self.assertEqual(part_1(self._eng), 4_361)

    def test_part_2(self):
        self.assertEqual(part_2(self._eng), 467_835)


if __name__ == '__main__':
    unittest.main()
