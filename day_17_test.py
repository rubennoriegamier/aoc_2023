from unittest import TestCase, main

from day_17 import part_1, part_2


class TestDay17(TestCase):
    _heat_maps: list[list[list[int]]]

    def setUp(self):
        self._heat_maps = [[list(map(int, line.rstrip())) for line in heat_map]
                           for heat_map in [['2413432311323',
                                             '3215453535623',
                                             '3255245654254',
                                             '3446585845452',
                                             '4546657867536',
                                             '1438598798454',
                                             '4457876987766',
                                             '3637877979653',
                                             '4654967986887',
                                             '4564679986453',
                                             '1224686865563',
                                             '2546548887735',
                                             '4322674655533'],
                                            ['111111111111',
                                             '999999999991',
                                             '999999999991',
                                             '999999999991',
                                             '999999999991']]]

    def test_part_1(self):
        self.assertEqual(part_1(self._heat_maps[0]), 102)

    def test_part_2(self):
        for i, (heat_map, path_len) in enumerate(zip(self._heat_maps, [94, 71])):
            with self.subTest(i=i):
                self.assertEqual(part_2(heat_map), path_len)


if __name__ == '__main__':
    main()
