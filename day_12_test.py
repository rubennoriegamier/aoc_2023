from unittest import TestCase, main

from day_12 import parse_row, part_2


class TestDay12(TestCase):
    _rows: list[tuple[str, tuple[int, ...]]]

    def setUp(self):
        self._rows = list(map(parse_row, ['???.### 1,1,3',
                                          '.??..??...?##. 1,1,3',
                                          '?#?#?#?#?#?#?#? 1,3,1,6',
                                          '????.#...#... 4,1,1',
                                          '????.######..#####. 1,6,5',
                                          '?###???????? 3,2,1']))

    def test_part_2(self):
        self.assertEqual(part_2(self._rows), 525_152)


if __name__ == '__main__':
    main()
