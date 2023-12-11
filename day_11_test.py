from unittest import TestCase, main

from day_11 import Image


class TestDay11(TestCase):
    _raw_image: list[str]

    def setUp(self):
        self._raw_image = ['...#......',
                           '.......#..',
                           '#.........',
                           '..........',
                           '......#...',
                           '.#........',
                           '.........#',
                           '..........',
                           '.......#..',
                           '#...#.....']

    def test_part_1(self):
        self.assertEqual(Image(self._raw_image).expand(2), 374)

    def test_part_2(self):
        for scale, result in zip([10, 100], [1_030, 8_410]):
            with self.subTest(item_type=scale):
                self.assertEqual(Image(self._raw_image).expand(scale), result)


if __name__ == '__main__':
    main()
