import fileinput
from itertools import accumulate, cycle
from math import lcm


def main():
    instructions: list[int] = list(map(parse_instruction, input()))
    input()
    nodes: dict[str, tuple[str, str]] = dict(map(parse_node, map(str.rstrip, fileinput.input())))

    print(part_1(instructions, nodes))
    print(part_2(instructions, nodes))


def parse_instruction(raw_instruction: str) -> int:
    return 0 if raw_instruction == 'L' else 1


def parse_node(raw_node: str) -> tuple[str, tuple[str, str]]:
    node, left_right = raw_node.split(' = ')

    return node, tuple(left_right[1:-1].split(', '))


def part_1(instructions: list[int], nodes: dict[str, tuple[str, str]]) -> int:
    return next(steps for steps, node in
                enumerate(accumulate(cycle(instructions),
                                     lambda node, instruction: nodes[node][instruction],
                                     initial='AAA'))
                if node == 'ZZZ')


def part_2(instructions: list[int], nodes: dict[str, tuple[str, str]]) -> int:
    return lcm(*(next(steps for steps, node in
                      enumerate(accumulate(cycle(instructions),
                                           lambda node_, instruction: nodes[node_][instruction],
                                           initial=node))
                      if node[-1] == 'Z')
                 for node in nodes
                 if node[-1] == 'A'))


if __name__ == '__main__':
    main()
