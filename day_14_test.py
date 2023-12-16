from unittest import TestCase, main

from day_14 import part_1, part_2


class TestDay14(TestCase):
    _platform: list[str]

    def setUp(self):
        self._platform = ['O....#....',
                          'O.OO#....#',
                          '.....##...',
                          'OO.#O....O',
                          '.O.....O#.',
                          'O.#..O.#.#',
                          '..O..#O..O',
                          '.......O..',
                          '#....###..',
                          '#OO..#....']

    def test_part_1(self):
        self.assertEqual(part_1(self._platform), 136)

    def test_part_2(self):
        self.assertEqual(part_2(self._platform), 64)


if __name__ == '__main__':
    main()
