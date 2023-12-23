import fileinput
from collections import defaultdict, deque
from itertools import groupby
from operator import itemgetter
from typing import NamedTuple, Self


def main():
    bricks = list(map(Brick.parse, map(str.rstrip, fileinput.input())))

    print(*part_1_and_2(bricks), sep='\n')


class Point(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def parse(cls, point: str) -> 'Point':
        return cls(*map(int, point.split(',')))


class Brick(NamedTuple):
    a: Point
    b: Point

    def below(self, brick: Self) -> bool:
        return self.b.z < brick.a.z

    def crosses(self, brick: Self) -> bool:
        return self.a.x <= brick.b.x and self.b.x >= brick.a.x and \
            self.a.y <= brick.b.y and self.b.y >= brick.a.y

    def fall(self, distance: int) -> Self:
        return Brick(Point(self.a.x, self.a.y, self.a.z - distance),
                     Point(self.b.x, self.b.y, self.b.z - distance))

    def fall_to(self, brick: Self | None = None) -> Self:
        return self.fall(self.a.z - brick.b.z - 1 if brick else self.a.z - 1)

    @classmethod
    def parse(cls, brick: str) -> Self:
        return cls(*map(Point.parse, brick.split('~')))


def part_1_and_2(bricks: list[Brick]) -> tuple[int, int]:
    bricks = sorted(bricks, key=lambda b: b.a.z)
    resting_bricks = []
    supported_by = {}
    supporting = defaultdict(list)

    for brick in bricks:
        if candidates := sorted((brick.a.z - resting_brick.b.z - 1, resting_brick)
                                for resting_brick in resting_bricks
                                if resting_brick.below(brick) and resting_brick.crosses(brick)):
            distance, support_bricks = next(groupby(candidates, key=itemgetter(0)))
            brick = brick.fall(distance)
            support_bricks = list(map(itemgetter(1), support_bricks))
            supported_by[brick] = support_bricks
            for support_brick in support_bricks:
                supporting[support_brick].append(brick)
            resting_bricks.append(brick)
        else:
            resting_bricks.append(brick.fall_to())

    part_1 = 0
    part_2 = 0

    for brick in resting_bricks:
        if all(len(supported_by[supported_brick]) > 1
               for supported_brick in supporting.get(brick, [])):
            part_1 += 1
        else:
            fallen_bricks = {brick}
            supported_bricks = deque(supporting[brick])

            while supported_bricks:
                supported_brick = supported_bricks.popleft()

                if all(supporting_brick in fallen_bricks
                       for supporting_brick in supported_by[supported_brick]):
                    fallen_bricks.add(supported_brick)
                    supported_bricks.extend(supporting[supported_brick])

            part_2 += len(fallen_bricks) - 1

    return part_1, part_2


if __name__ == '__main__':
    main()
