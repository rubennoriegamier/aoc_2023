import fileinput
from collections.abc import Generator
from functools import reduce
from operator import lt, mul, gt
from typing import Callable


def main():
    workflows, parts = ''.join(fileinput.input()).split('\n\n')
    workflows = dict(map(Workflow.parse, workflows.splitlines()))
    parts = list(map(parse_part, parts.splitlines()))

    print(part_1(workflows, parts))
    print(part_2(workflows))


class Rule:
    _OPS = {'<': lt, '>': gt}

    _then: str
    _cat: str | None = None
    _op: str | None = None
    _val: int | None = None
    _f: Callable[[dict[str, int]], str | None]

    def __init__(self, rule: str):
        if ':' in rule:
            if_, self._then = rule.split(':')
            self._cat = if_[0]
            self._op = if_[1]
            self._val = int(if_[2:])

            self._f = lambda part: self._then if self._OPS[self._op](part[self._cat], self._val) else None
        else:
            self._then = rule
            self._f = lambda _: rule

    def __call__(self, part: dict[str, int]) -> str | None:
        return self._f(part)

    def split(self, part: dict[str, range]) -> Generator[tuple[str | None, dict[str, range]]]:
        t_range = None
        f_range = None

        match self._op:
            case None:
                yield self._then, part
            case '<':
                cat_range = part[self._cat]
                t_range = range(cat_range.start, min(cat_range.stop, self._val))
                f_range = range(max(cat_range.start, self._val), cat_range.stop)
            case '>':
                cat_range = part[self._cat]
                t_range = range(max(cat_range.start, self._val + 1), cat_range.stop)
                f_range = range(cat_range.start, min(cat_range.stop, self._val + 1))

        if t_range:
            yield self._then, {cat: t_range if cat == self._cat else range_
                               for cat, range_ in part.items()}
        if f_range:
            yield None, {cat: f_range if cat == self._cat else range_
                         for cat, range_ in part.items()}


class Workflow:
    _rules: list[Rule]

    def __init__(self, rules: list[Rule]):
        self._rules = rules.copy()

    @classmethod
    def parse(cls, workflow: str) -> tuple[str, 'Workflow']:
        name, rules = workflow.split('{')

        return name, cls(list(map(Rule, rules[:-1].split(','))))

    def __call__(self, part: dict[str, int]) -> str:
        return next(filter(None, (rule(part) for rule in self._rules)))

    def split(self, part: dict[str, range]) -> Generator[tuple[str, dict[str, range]]]:
        parts = [part]

        for rule in self._rules:
            for name, part_ in rule.split(parts.pop()):
                if name:
                    yield name, part_
                else:
                    parts.append(part_)
            if not parts:
                break


def parse_part(part: str) -> dict[str, int]:
    return {cat[0]: int(cat[2:]) for cat in part[1:-1].split(',')}


def part_1(workflows: dict[str, Workflow], parts: list[dict[str, int]]) -> int:
    rating = 0

    for part in parts:
        name = 'in'

        while True:
            match name := workflows[name](part):
                case 'A':
                    rating += sum(part.values())
                    break
                case 'R':
                    break

    return rating


def part_2(workflows: dict[str, Workflow]) -> int:
    combinations = 0
    parts = [('in', {'x': range(1, 4_001), 'm': range(1, 4_001), 'a': range(1, 4_001), 's': range(1, 4_001)})]

    while parts:
        name, part = parts.pop()

        for name, part in workflows[name].split(part):
            if name == 'A':
                combinations += reduce(mul, map(len, part.values()))
            elif name != 'R':
                parts.append((name, part))

    return combinations


if __name__ == '__main__':
    main()
