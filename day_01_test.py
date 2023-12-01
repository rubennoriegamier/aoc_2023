import unittest

from day_01 import part_1, part_2


class TestDay01(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1(['1abc2',
                                 'pqr3stu8vwx',
                                 'a1b2c3d4e5f',
                                 'treb7uchet']), 142)

    def test_part_2(self):
        self.assertEqual(part_2(['two1nine',
                                 'eightwothree',
                                 'abcone2threexyz',
                                 'xtwone3four',
                                 '4nineeightseven2',
                                 'zoneight234',
                                 '7pqrstsixteen',
                                 '2twoneh']), 302)


if __name__ == '__main__':
    unittest.main()
