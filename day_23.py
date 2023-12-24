import fileinput
from functools import cache

import networkx as nx
from igraph import Graph


def main():
    grid = list(map(str.rstrip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str]) -> int:
    vs = []

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile != '#':
                vs.append((y, x))

    g = Graph(len(vs), directed=True)
    vs = {v: i for i, v in enumerate(vs)}
    es = []

    for (y, x), i in vs.items():
        match grid[y][x]:
            case '.':
                if grid[y][x + 1] in '.>':
                    es.append((i, vs[y, x + 1]))
                if y < len(grid) - 1 and grid[y + 1][x] in '.v':
                    es.append((i, vs[y + 1, x]))
                if grid[y][x - 1] in '.<':
                    es.append((i, vs[y, x - 1]))
                if y > 0 and grid[y - 1][x] in '.^':
                    es.append((i, vs[y - 1, x]))
            case '>':
                es.append((i, vs[y, x + 1]))
            case 'v':
                es.append((i, vs[y + 1, x]))
            case '<':
                es.append((i, vs[y, x - 1]))
            case '^':
                es.append((i, vs[y - 1, x]))
            case _:
                raise NotImplementedError

    g.add_edges(es)

    return max(map(len, g.get_all_simple_paths(0, len(vs) - 1))) - 1


def part_2(grid: list[str]) -> int:
    g = nx.Graph()
    vs = {(y, x): y << 8 | x
          for y, row in enumerate(grid)
          for x, tile in enumerate(row)
          if tile != '#'}

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile != '#':
                if grid[y][x + 1] != '#':
                    g.add_edge(vs[y, x], vs[y, x + 1], weight=1)
                    # g.add_edge((y, x), (y, x + 1), weight=1)
                if y < len(grid) - 1 and grid[y + 1][x] != '#':
                    g.add_edge(vs[y, x], vs[y + 1, x], weight=1)
                    # g.add_edge((y, x), (y + 1, x), weight=1)

    while True:
        for node in g.nodes:
            if len(neighbors := g[node]) == 2:
                weight = sum(attrs['weight'] for attrs in neighbors.values())
                g.add_edge(*neighbors, weight=weight)
                g.remove_node(node)
                break
        else:
            break

    end = vs[len(grid) - 1, len(grid[0]) - 2]
    es = {v: [(neighbor, attrs['weight']) for neighbor, attrs in g[v].items()] for v in g}

    @cache
    def path_length(path: tuple[int, ...]) -> int | None:
        last = path[-1]
        if last == end:
            return 0
        path = tuple(sorted(path))

        max_length = None

        # noinspection PyShadowingNames
        for neighbor, weight in es[last]:
            if neighbor not in path:
                if (length := path_length(path + (neighbor,))) is not None:
                    if max_length is None:
                        max_length = weight + length
                    else:
                        max_length = max(weight + length, max_length)

        return max_length

    return path_length((vs[0, 1],))


if __name__ == '__main__':
    main()
