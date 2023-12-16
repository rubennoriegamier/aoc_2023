from unittest import TestCase, main

from day_13 import summarize, summarize_with_smudge


class TestDay13(TestCase):
    _patterns: list[list[str]]

    def setUp(self):
        self._patterns = [['#.##..##.',
                           '..#.##.#.',
                           '##......#',
                           '##......#',
                           '..#.##.#.',
                           '..##..##.',
                           '#.#.##.#.'],
                          ['#...##..#',
                           '#....#..#',
                           '..##..###',
                           '#####.##.',
                           '#####.##.',
                           '..##..###',
                           '#....#..#']]

    def test_summarize(self):
        for i, (pattern, summary) in enumerate(zip(self._patterns, [5, 400])):
            with self.subTest(i=i):
                self.assertEqual(summarize(pattern), summary)

    def test_summarize_with_sumdge(self):
        for i, (pattern, summary) in enumerate(zip(self._patterns, [300, 100])):
            with self.subTest(i=i):
                self.assertEqual(summarize_with_smudge(pattern), summary)


if __name__ == '__main__':
    main()
