from unittest import TestCase, main

from day_15 import part_1, part_2


class TestDay15(TestCase):
    _steps: list[str]

    def setUp(self):
        self._steps = ['rn=1',
                       'cm-',
                       'qp=3',
                       'cm=2',
                       'qp-',
                       'pc=4',
                       'ot=9',
                       'ab=5',
                       'pc-',
                       'pc=6',
                       'ot=7']

    def test_part_1(self):
        self.assertEqual(part_1(self._steps), 1_320)

    def test_part_2(self):
        self.assertEqual(part_2(self._steps), 145)


if __name__ == '__main__':
    main()
