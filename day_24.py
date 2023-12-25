import fileinput
from itertools import combinations
from typing import NamedTuple, Self

import sympy as sym
from shapely import LineString, Point


def main():
    hailstones = list(map(parse_hailstone, fileinput.input()))

    print(part_1(hailstones, least=200_000_000_000_000, most=400_000_000_000_000))
    print(part_2(hailstones))


class Position(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def parse(cls, raw_pos: str) -> Self:
        return cls(*map(int, raw_pos.split(', ')))


class Velocity(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def parse(cls, raw_vel: str) -> Self:
        return cls(*map(int, raw_vel.split(', ')))


def parse_hailstone(hailstone: str) -> tuple[Position, Velocity]:
    position, velocity = hailstone.split(' @ ')

    return Position.parse(position), Velocity.parse(velocity)


def part_1(hailstones: list[tuple[Position, Velocity]], *, least: int, most: int) -> int:
    segments = [LineString([(p.x, p.y), (p.x + v.x * most, p.y + v.y * most)]) for p, v in hailstones]

    return sum(least <= i.x <= most and least <= i.y <= most
               for s_1, s_2 in combinations(segments, 2)
               if isinstance(i := s_1.intersection(s_2), Point))


def part_2(hailstones: list[tuple[Position, Velocity]]) -> int:
    px, py, pz, vx, vy, vz = [sym.Symbol(name) for name in ['px', 'py', 'pz', 'vx', 'vy', 'vz']]
    ts = [sym.Symbol(f't_{i}') for i in range(3)]
    eqns = []

    for ((h_px, h_py, h_pz), (h_vx, h_vy, h_vz)), t in zip(hailstones[:3], ts):
        eqns.append(sym.Eq(px + vx * t, h_px + h_vx * t))
        eqns.append(sym.Eq(py + vy * t, h_py + h_vy * t))
        eqns.append(sym.Eq(pz + vz * t, h_pz + h_vz * t))

    return sum(sym.solve(eqns, [px, py, pz, vx, vy, vz] + ts)[0][:3])


if __name__ == '__main__':
    main()
