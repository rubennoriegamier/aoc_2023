from unittest import TestCase, main

from day_21 import Garden


class TestDay21(TestCase):
    _garden: Garden

    def setUp(self):
        self._garden = Garden(['...........',
                               '.....###.#.',
                               '.###.##..#.',
                               '..#.#...#..',
                               '....#.#....',
                               '.##..S####.',
                               '.##..#...#.',
                               '.......##..',
                               '.##.#.####.',
                               '.##..##.##.',
                               '...........'])

    def test_part_1(self):
        self.assertEqual(self._garden.part_1(6), 16)


if __name__ == '__main__':
    main()
