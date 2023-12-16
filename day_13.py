import fileinput
from operator import ne


def main():
    patterns = list(map(str.split, ''.join(fileinput.input()).split('\n\n')))

    print(part_1(patterns))
    print(part_2(patterns))


def summarize(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        size = min(i, len(pattern) - i)

        if pattern[i - size:i] == pattern[i:i + size][::-1]:
            return i * 100

    return summarize(list(zip(*pattern))) // 100


def summarize_with_smudge(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        size = min(i, len(pattern) - i)
        smudge = False

        for row_a, row_b in zip(pattern[i - size:i], pattern[i:i + size][::-1]):
            if row_a != row_b:
                if smudge or sum(map(ne, row_a, row_b)) > 1:
                    break
                smudge = True
        else:
            if smudge:
                return i * 100

    return summarize_with_smudge(list(zip(*pattern))) // 100


def part_1(patterns: list[list[str]]) -> int:
    return sum(map(summarize, patterns))


def part_2(patterns: list[list[str]]) -> int:
    return sum(map(summarize_with_smudge, patterns))


if __name__ == '__main__':
    main()
