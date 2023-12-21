import fileinput
from collections import defaultdict, deque
from itertools import count
from math import lcm
from operator import methodcaller


def main():
    mods = list(map(str.rstrip, fileinput.input()))

    print(part_1(mods))
    print(part_2(mods))


class Circuit:
    _outs: dict[str, list[str]]
    _types: dict[str, str]
    _ff_state: dict[str, bool]
    _co_state: defaultdict[str, dict[str, bool]]

    def __init__(self, mods: list[str]):
        self._outs = {}
        self._types = {}
        self._ff_state = {}
        self._co_state = defaultdict(dict)

        for name, outs in map(methodcaller('split', ' -> '), mods):
            outs = outs.split(', ')

            match name[0]:
                case 'b':
                    self._outs[name] = outs
                case '%':
                    name = name[1:]

                    self._outs[name] = outs
                    self._types[name] = '%'
                    self._ff_state[name] = False
                case '&':
                    name = name[1:]

                    self._outs[name] = outs
                    self._types[name] = '&'
                case _:
                    raise NotImplementedError

        for in_, outs in self._outs.items():
            for out in outs:
                if self._types.get(out) == '&':
                    self._co_state[out][in_] = False

    def push_button(self) -> tuple[int, int]:
        low = 1
        high = 0

        pulses = deque(('broadcaster', False, out) for out in self._outs['broadcaster'])

        while pulses:
            in_, pulse, out = pulses.popleft()

            if pulse:
                high += 1
            else:
                low += 1

            match self._types.get(out):
                case '%':
                    if not pulse:
                        pulse = not self._ff_state[out]
                        self._ff_state[out] = pulse
                        pulses.extend((out, pulse, next_out) for next_out in self._outs[out])
                case '&':
                    self._co_state[out][in_] = pulse
                    pulse = not all(self._co_state[out].values())
                    pulses.extend((out, pulse, next_out) for next_out in self._outs[out])

        return low, high

    def find_rx(self):
        rx_prev = next(mod for mod, outs in self._outs.items() if outs[0] == 'rx')
        rx_prev = [mod for mod, outs in self._outs.items() if outs[0] == rx_prev]
        result = 1

        for n in count(1):
            pulses = deque(('broadcaster', False, out) for out in self._outs['broadcaster'])

            while pulses:
                in_, pulse, out = pulses.popleft()

                match self._types.get(out):
                    case '%':
                        if not pulse:
                            pulse = not self._ff_state[out]
                            self._ff_state[out] = pulse
                            pulses.extend((out, pulse, next_out) for next_out in self._outs[out])
                    case '&':
                        self._co_state[out][in_] = pulse
                        pulse = not all(self._co_state[out].values())
                        if pulse and out in rx_prev:
                            rx_prev.remove(out)
                            result = lcm(result, n)
                            if not rx_prev:
                                return result

                        pulses.extend((out, pulse, next_out) for next_out in self._outs[out])


def part_1(mods: list[str]) -> int:
    circuit = Circuit(mods)
    total_low = 0
    total_high = 0

    for _ in range(1_000):
        low, high = circuit.push_button()
        total_low += low
        total_high += high

    return total_low * total_high


def part_2(mods: list[str]) -> int:
    circuit = Circuit(mods)

    return circuit.find_rx()


if __name__ == '__main__':
    main()
