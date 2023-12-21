from unittest import TestCase, main

from day_20 import part_1


class TestDay20(TestCase):
    _mods: list[list[str]]

    def setUp(self):
        self._mods = [['broadcaster -> a, b, c',
                       '%a -> b',
                       '%b -> c',
                       '%c -> inv',
                       '&inv -> a'],
                      ['broadcaster -> a',
                       '%a -> inv, con',
                       '&inv -> b',
                       '%b -> con',
                       '&con -> output']]

    def test_part_1(self):
        for i, (mods, result) in enumerate(zip(self._mods, [32_000_000, 11_687_500])):
            with self.subTest(i=i):
                self.assertEqual(part_1(mods), result)


if __name__ == '__main__':
    main()
