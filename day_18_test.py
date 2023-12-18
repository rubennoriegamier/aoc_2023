from unittest import TestCase, main

from day_18 import Dig, part_1, part_2


class TestDay18(TestCase):
    _dig_plan: list[Dig]

    def setUp(self):
        self._dig_plan = list(map(Dig.parse, ['R 6 (#70c710)',
                                              'D 5 (#0dc571)',
                                              'L 2 (#5713f0)',
                                              'D 2 (#d2c081)',
                                              'R 2 (#59c680)',
                                              'D 2 (#411b91)',
                                              'L 5 (#8ceee2)',
                                              'U 2 (#caa173)',
                                              'L 1 (#1b58a2)',
                                              'U 2 (#caa171)',
                                              'R 2 (#7807d2)',
                                              'U 3 (#a77fa3)',
                                              'L 2 (#015232)',
                                              'U 2 (#7a21e3)']))

    def test_part_1(self):
        self.assertEqual(part_1(self._dig_plan), 62)

    def test_part_2(self):
        self.assertEqual(part_2(self._dig_plan), 952_408_144_115)


if __name__ == '__main__':
    main()
