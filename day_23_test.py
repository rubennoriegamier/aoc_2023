from unittest import TestCase, main

from day_23 import part_1, part_2


class TestDay23(TestCase):
    _grid: list[str]

    def setUp(self):
        self._grid = ['#.#####################',
                      '#.......#########...###',
                      '#######.#########.#.###',
                      '###.....#.>.>.###.#.###',
                      '###v#####.#v#.###.#.###',
                      '###.>...#.#.#.....#...#',
                      '###v###.#.#.#########.#',
                      '###...#.#.#.......#...#',
                      '#####.#.#.#######.#.###',
                      '#.....#.#.#.......#...#',
                      '#.#####.#.#.#########v#',
                      '#.#...#...#...###...>.#',
                      '#.#.#v#######v###.###v#',
                      '#...#.>.#...>.>.#.###.#',
                      '#####v#.#.###v#.#.###.#',
                      '#.....#...#...#.#.#...#',
                      '#.#########.###.#.#.###',
                      '#...###...#...#...#.###',
                      '###.###.#.###v#####v###',
                      '#...#...#.#.>.>.#.>.###',
                      '#.###.###.#.###.#.#v###',
                      '#.....###...###...#...#',
                      '#####################.#']

    def test_part_1(self):
        self.assertEqual(part_1(self._grid), 94)

    def test_part_2(self):
        self.assertEqual(part_2(self._grid), 154)


if __name__ == '__main__':
    main()