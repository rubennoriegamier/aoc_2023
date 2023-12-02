import unittest

from day_02 import RGB, parse_game, part_1, part_2


class TestDay02(unittest.TestCase):
    _raw_games: list[str]

    def setUp(self):
        self._raw_games = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                           'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                           'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                           'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                           'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

    def test_parse_full_rgb(self):
        self.assertEqual(RGB.parse('3 green, 4 blue, 1 red'), RGB(1, 3, 4))

    def test_parse_partial_rgb(self):
        self.assertEqual(RGB.parse('3 blue, 4 red'), RGB(4, 0, 3))

    def test_parse_game(self):
        self.assertEqual(parse_game(self._raw_games[2]), [RGB(20, 8, 6), RGB(4, 13, 5), RGB(1, 5, 0)])

    def test_part_1(self):
        self.assertEqual(part_1(list(map(parse_game, self._raw_games))), 8)

    def test_part_2(self):
        self.assertEqual(part_2(list(map(parse_game, self._raw_games))), 2_286)


if __name__ == '__main__':
    unittest.main()
