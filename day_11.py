import fileinput
from itertools import combinations, pairwise


def main():
    image = Image(list(map(str.rstrip, fileinput.input())))

    print(image.expand(2))
    print(image.expand(500_000))


class Image:
    _galaxies: list[tuple[int, int]]

    def __init__(self, raw_image: list[str]):
        self._galaxies = [(y, x)
                          for y, row in enumerate(raw_image)
                          for x, tile in enumerate(row)
                          if tile == '#']

    def __str__(self):
        max_y = 0
        max_x = 0

        for y, x in self._galaxies:
            max_y = max(max_y, y)
            max_x = max(max_x, x)

        image = [['.'] * (max_x + 1) for _ in range(max_y + 1)]

        for y, x in self._galaxies:
            image[y][x] = '#'

        return '\n'.join(map(''.join, image))

    def _y_expand(self, scale: int):
        galaxies = []
        offset = 0

        self._galaxies.sort()
        galaxies.append(self._galaxies[0])

        for (y_1, _), (y_2, x_2) in pairwise(self._galaxies):
            spaces = max(y_2 - y_1 - 1, 0)
            galaxies.append((offset + y_2 + spaces * (scale - 1), x_2))
            offset += spaces * (scale - 1)

        self._galaxies = galaxies

    def _x_expand(self, scale: int):
        galaxies = []
        offset = 0

        self._galaxies.sort(key=lambda galaxy: galaxy[::-1])
        galaxies.append(self._galaxies[0])

        for (_, x_1), (y_2, x_2) in pairwise(self._galaxies):
            spaces = max(x_2 - x_1 - 1, 0)
            galaxies.append((y_2, offset + x_2 + spaces * (scale - 1)))
            offset += spaces * (scale - 1)

        self._galaxies = galaxies

    def expand(self, scale: int) -> int:
        self._y_expand(scale)
        self._x_expand(scale)

        return sum(abs(y_1 - y_2) + abs(x_1 - x_2)
                   for (y_1, x_1), (y_2, x_2) in combinations(self._galaxies, 2))


if __name__ == '__main__':
    main()
