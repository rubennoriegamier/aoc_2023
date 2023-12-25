from unittest import TestCase, main

from day_24 import Position, Velocity, parse_hailstone, part_1, part_2


class TestDay24(TestCase):
    _hailstones: list[tuple[Position, Velocity]]

    def setUp(self):
        self._hailstones = list(map(parse_hailstone, ['19, 13, 30 @ -2,  1, -2',
                                                      '18, 19, 22 @ -1, -1, -2',
                                                      '20, 25, 34 @ -2, -2, -4',
                                                      '12, 31, 28 @ -1, -2, -1',
                                                      '20, 19, 15 @  1, -5, -3']))

    def test_part_1(self):
        self.assertEqual(part_1(self._hailstones, least=7, most=27), 2)

    def test_part_2(self):
        self.assertEqual(part_2(self._hailstones), 47)


if __name__ == '__main__':
    main()
