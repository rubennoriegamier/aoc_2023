import fileinput
from collections import Counter
from itertools import pairwise
from operator import itemgetter, mul

import networkx as nx


def main():
    components = components_graph(list(map(str.rstrip, fileinput.input())))

    print(part_1(components))


def components_graph(es: list[str]) -> nx.Graph:
    components = nx.Graph()

    for e in es:
        v, vs = e.split(': ')

        for v_ in vs.split():
            components.add_edge(v, v_)

    return components


def part_1(components: nx.Graph) -> int:
    counter = Counter()

    for _, paths in nx.all_pairs_shortest_path(components):
        for path in paths.values():
            for pair in pairwise(path):
                counter[tuple(sorted(pair))] += 1

    components.remove_edges_from(map(itemgetter(0), counter.most_common(3)))

    return mul(*map(len, nx.connected_components(components)))


if __name__ == '__main__':
    main()
