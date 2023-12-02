import fileinput
from functools import reduce
from operator import mul
from typing import NamedTuple


def main():
    games: list[list[RGB]] = list(map(parse_game, map(str.rstrip, fileinput.input())))

    print(part_1(games))
    print(part_2(games))


class RGB(NamedTuple):
    r: int
    g: int
    b: int

    @classmethod
    def parse(cls, raw_rgb: str) -> 'RGB':
        r = 0
        g = 0
        b = 0

        for val, color in map(str.split, raw_rgb.split(', ')):
            match color:
                case 'red':
                    r = int(val)
                case 'green':
                    g = int(val)
                case 'blue':
                    b = int(val)
                case _:
                    raise NotImplementedError

        return cls(r, g, b)


def parse_game(raw_game: str) -> list[RGB]:
    return list(map(RGB.parse, raw_game.split(': ')[1].split('; ')))


def part_1(games: list[list[RGB]]) -> int:
    return sum(idx for idx, game in enumerate(games, 1)
               if all(rgb.r <= 12 and
                      rgb.g <= 13 and
                      rgb.b <= 14
                      for rgb in game))


def part_2(games: list[list[RGB]]) -> int:
    return sum(reduce(mul, map(max, zip(*game)))
               for game in games)


if __name__ == '__main__':
    main()
