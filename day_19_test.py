from unittest import TestCase, main

from day_19 import Workflow, parse_part, part_1, part_2


class TestDay19(TestCase):
    _workflows: dict[str, Workflow]
    _parts: list[dict[str, int]]

    def setUp(self):
        self._workflows = dict(map(Workflow.parse, ['px{a<2006:qkq,m>2090:A,rfg}',
                                                    'pv{a>1716:R,A}',
                                                    'lnx{m>1548:A,A}',
                                                    'rfg{s<537:gd,x>2440:R,A}',
                                                    'qs{s>3448:A,lnx}',
                                                    'qkq{x<1416:A,crn}',
                                                    'crn{x>2662:A,R}',
                                                    'in{s<1351:px,qqz}',
                                                    'qqz{s>2770:qs,m<1801:hdj,R}',
                                                    'gd{a>3333:R,R}',
                                                    'hdj{m>838:A,pv}']))
        self._parts = list(map(parse_part, ['{x=787,m=2655,a=1222,s=2876}',
                                            '{x=1679,m=44,a=2067,s=496}',
                                            '{x=2036,m=264,a=79,s=2244}',
                                            '{x=2461,m=1339,a=466,s=291}',
                                            '{x=2127,m=1623,a=2188,s=1013}']))

    def test_part_1(self):
        self.assertEqual(part_1(self._workflows, self._parts), 19_114)

    def test_part_2(self):
        self.assertEqual(part_2(self._workflows), 167_409_079_868_000)


if __name__ == '__main__':
    main()
