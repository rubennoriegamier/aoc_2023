import fileinput
from operator import methodcaller
from typing import NamedTuple, Self

import sympy as sym


def main():
    hailstones = [(Position.parse(raw_pos), Velocity.parse(raw_vel))
                  for raw_pos, raw_vel in map(methodcaller('split', ' @ '), fileinput.input())]

    print(part_3(hailstones))


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


def part_3(hailstones: list[tuple[Position, Velocity]]) -> int:
    px, py, pz, vx, vy, vz = [sym.Symbol(name) for name in ['px', 'py', 'pz', 'vx', 'vy', 'vz']]
    ts = [sym.Symbol(f't_{i}') for i in range(len(hailstones))]
    eqns = []

    for ((h_px, h_py, h_pz), (h_vx, h_vy, h_vz)), t in zip(hailstones, ts):
        eqns.append(sym.Eq(px + vx * t, h_px + h_vx * t))
        eqns.append(sym.Eq(py + vy * t, h_py + h_vy * t))
        eqns.append(sym.Eq(pz + vz * t, h_pz + h_vz * t))

    print(sym.solve(eqns, [px, py, pz, vx, vy, vz] + ts))


if __name__ == '__main__':
    main()
