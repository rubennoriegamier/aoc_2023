import fileinput
import itertools as it
from functools import partial, reduce


def main():
    seeds, maps = parse_almanac(''.join(fileinput.input()))

    print(part_1(seeds, maps))
    print(part_2(seeds, maps))


def parse_almanac(raw_almanac: str) -> tuple[list[int], list[list[tuple[range, range]]]]:
    raw_seeds, raw_maps = raw_almanac.split('\n\n', 1)
    seeds = list(map(int, raw_seeds.split(': ')[1].split()))
    maps = list(map(parse_map, raw_maps.split('\n\n')))

    return seeds, maps


def parse_map(raw_map: str) -> list[tuple[range, range]]:
    return [(range(dst_start, dst_start + length),
             range(src_start, src_start + length))
            for dst_start, src_start, length
            in map(partial(map, int),
                   map(str.split, raw_map.split(':\n')[1].splitlines()))]


def part_1(seeds: list[int], maps: list[list[tuple[range, range]]]) -> int:
    def location(n: int, i: int = 0) -> int:
        return n if i == len(maps) else location(next((n - src_range.start + dst_range.start
                                                       for dst_range, src_range in maps[i]
                                                       if n in src_range), n), i + 1)

    return min(map(location, seeds))


def part_2(seeds: list[int], maps: list[list[tuple[range, range]]]) -> int:
    seed_ranges = [range(start, start + length)
                   for start, length in it.batched(seeds, 2)]
    comb_maps = reduce(combine_maps, maps)

    return min(dst_range.start + max(seed_range.start - src_range.start, 0)
               for seed_range in seed_ranges
               for dst_range, src_range in comb_maps
               if src_range.stop > seed_range.start and src_range.start < seed_range.stop)


def combine_maps(maps_a: list[tuple[range, range]], maps_b: list[tuple[range, range]]) -> list[tuple[range, range]]:
    maps_a = sorted(maps_a, key=lambda ranges: ranges[1].start)
    maps_b = sorted(maps_b, key=lambda ranges: ranges[1].start)
    maps_c = []

    if (start := maps_b[0][1].start) < (stop := maps_a[0][1].start):
        maps_a.insert(0, (range(start, stop), range(start, stop)))
    if (start := maps_a[-1][1].stop) < (stop := maps_b[-1][1].stop):
        maps_a.append((range(start, stop), range(start, stop)))

    for dst_range_a, src_range_a in maps_a:
        if overlaps := list(it.takewhile(lambda map_b: map_b[1].start < dst_range_a.stop,
                                         it.dropwhile(lambda map_b: map_b[1].stop <= dst_range_a.start, maps_b))):
            if dst_range_c := range(dst_range_a.start, overlaps[0][1].start):
                src_range_c = range(src_range_a.start, src_range_a.start + len(dst_range_c))
                maps_c.append((dst_range_c, src_range_c))
            for dst_range_b, src_range_b in overlaps:
                overlap = min(dst_range_a.stop, src_range_b.stop) - max(dst_range_a.start, src_range_b.start)
                dst_start_c = dst_range_b.start + max(dst_range_a.start - src_range_b.start, 0)
                dst_range_c = range(dst_start_c, dst_start_c + overlap)
                src_start_c = src_range_a.start + max(src_range_b.start - dst_range_a.start, 0)
                src_range_c = range(src_start_c, src_start_c + overlap)
                maps_c.append((dst_range_c, src_range_c))
            if dst_range_c := range(overlaps[-1][1].stop, dst_range_a.stop):
                src_range_c = range(src_range_a.stop - len(dst_range_c), src_range_a.stop)
                maps_c.append((dst_range_c, src_range_c))
        else:
            maps_c.append((dst_range_a, src_range_a))

    return maps_c


if __name__ == '__main__':
    main()
