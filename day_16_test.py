from unittest import TestCase, main

from day_16 import part_1, part_2


class TestDay16(TestCase):
    _grid: list[str]

    def setUp(self):
        self._grid = ['.|...\\....',
                      '|.-.\\.....',
                      '.....|-...',
                      '........|.',
                      '..........',
                      '.........\\',
                      '..../.\\\\..',
                      '.-.-/..|..',
                      '.|....-|.\\',
                      '..//.|....']

    def test_part_1(self):
        self.assertEqual(part_1(self._grid), 46)

    def test_part_2(self):
        self.assertEqual(part_2(self._grid), 51)


if __name__ == '__main__':
    main()
