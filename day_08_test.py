from unittest import TestCase, main

from day_08 import parse_instruction, parse_node, part_1, part_2


class TestDay08(TestCase):
    def test_part_1(self):
        instructions = list(map(parse_instruction, 'LLR'))
        nodes = dict(map(parse_node, ['AAA = (BBB, BBB)',
                                      'BBB = (AAA, ZZZ)',
                                      'ZZZ = (ZZZ, ZZZ)']))

        self.assertEqual(part_1(instructions, nodes), 6)

    def test_part_2(self):
        instructions = list(map(parse_instruction, 'LR'))
        nodes = dict(map(parse_node, ['11A = (11B, XXX)',
                                      '11B = (XXX, 11Z)',
                                      '11Z = (11B, XXX)',
                                      '22A = (22B, XXX)',
                                      '22B = (22C, 22C)',
                                      '22C = (22Z, 22Z)',
                                      '22Z = (22B, 22B)',
                                      'XXX = (XXX, XXX)']))

        self.assertEqual(part_2(instructions, nodes), 6)


if __name__ == '__main__':
    main()
