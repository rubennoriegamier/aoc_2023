from unittest import TestCase, main

from day_22 import Brick, part_1_and_2


class TestDay22(TestCase):
    _bricks: list[Brick]

    def setUp(self):
        self._bricks = list(map(Brick.parse, ['1,0,1~1,2,1',
                                              '0,0,2~2,0,2',
                                              '0,2,3~2,2,3',
                                              '0,0,4~0,2,4',
                                              '2,0,5~2,2,5',
                                              '0,1,6~2,1,6',
                                              '1,1,8~1,1,9']))

    def test_part_1_and_2(self):
        part_1, part_2 = part_1_and_2(self._bricks)

        with self.subTest(part=1):
            self.assertEqual(part_1, 5)

        with self.subTest(part=2):
            self.assertEqual(part_2, 7)


if __name__ == '__main__':
    main()
