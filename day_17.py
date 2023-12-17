import fileinput

from igraph import Graph


def main():
    heat_map = [list(map(int, line.rstrip())) for line in fileinput.input()]

    print(part_1(heat_map))
    print(part_2(heat_map))


def create_graph(heat_map: list[list[int]], *, min_dist: int, max_dist: int) -> Graph:
    h = len(heat_map)
    w = len(heat_map[0])
    br_y = h - 1
    br_x = w - 1
    vs = [(-1, -1, 'tl', -1),
          (-1, -1, 'br', -1)]

    for y in range(h):
        for x in range(w):
            for dist in range(1, min(x + 1, max_dist + 1)):
                vs.append((y, x, '>', dist))
            for dist in range(1, min(y + 1, max_dist + 1)):
                vs.append((y, x, 'v', dist))
            for dist in range(1, min(w - x, max_dist + 1)):
                vs.append((y, x, '<', dist))
            for dist in range(1, min(h - y, max_dist + 1)):
                vs.append((y, x, '^', dist))

    g = Graph(directed=True)
    g.add_vertices(vs)
    get_v = {v: i for i, v in enumerate(vs)}

    tl = get_v[vs[0]]
    br = get_v[vs[1]]
    es = [(tl, get_v[0, 1, '>', 1]),
          (tl, get_v[1, 0, 'v', 1])]
    ws = [heat_map[0][1], heat_map[1][0]]
    for dist in range(1, min(max_dist + 1, w)):
        es.append((get_v[br_y, br_x, '>', dist], br))
        ws.append(0)
    for dist in range(1, min(max_dist + 1, h)):
        es.append((get_v[br_y, br_x, 'v', dist], br))
        ws.append(0)

    for (y, x, dir_, dist), v in get_v.items():
        match dir_:
            case '>':
                if dist >= min_dist:
                    if y >= min_dist:
                        es.append((v, get_v[y - 1, x, '^', 1]))
                        ws.append(heat_map[y - 1][x])
                    if y <= br_y - min_dist:
                        es.append((v, get_v[y + 1, x, 'v', 1]))
                        ws.append(heat_map[y + 1][x])
                if x < br_x and dist < max_dist:
                    es.append((v, get_v[y, x + 1, '>', dist + 1]))
                    ws.append(heat_map[y][x + 1])
            case 'v':
                if dist >= min_dist:
                    if x >= min_dist:
                        es.append((v, get_v[y, x - 1, '<', 1]))
                        ws.append(heat_map[y][x - 1])
                    if x <= br_x - min_dist:
                        es.append((v, get_v[y, x + 1, '>', 1]))
                        ws.append(heat_map[y][x + 1])
                if y < br_y and dist < max_dist:
                    es.append((v, get_v[y + 1, x, 'v', dist + 1]))
                    ws.append(heat_map[y + 1][x])
            case '<':
                if dist >= min_dist:
                    if y >= min_dist:
                        es.append((v, get_v[y - 1, x, '^', 1]))
                        ws.append(heat_map[y - 1][x])
                    if y <= br_y - min_dist:
                        es.append((v, get_v[y + 1, x, 'v', 1]))
                        ws.append(heat_map[y + 1][x])
                if x > 0 and dist < max_dist:
                    es.append((v, get_v[y, x - 1, '<', dist + 1]))
                    ws.append(heat_map[y][x - 1])
            case '^':
                if dist >= min_dist:
                    if x >= min_dist:
                        es.append((v, get_v[y, x - 1, '<', 1]))
                        ws.append(heat_map[y][x - 1])
                    if x <= br_x - min_dist:
                        es.append((v, get_v[y, x + 1, '>', 1]))
                        ws.append(heat_map[y][x + 1])
                if y > 0 and dist < max_dist:
                    es.append((v, get_v[y - 1, x, '^', dist + 1]))
                    ws.append(heat_map[y - 1][x])

    g.add_edges(es, {'weight': ws})

    return g


def path_len(heat_map: list[list[int]], *, min_dist: int, max_dist: int) -> int:
    g = create_graph(heat_map, min_dist=min_dist, max_dist=max_dist)
    es = g.get_shortest_path(g.vs.find(name=(-1, -1, 'tl', -1)),
                             g.vs.find(name=(-1, -1, 'br', -1)),
                             weights=g.es['weight'], output='epath')

    return sum(g.es[e]['weight'] for e in es)


def part_1(heat_map: list[list[int]]) -> int:
    return path_len(heat_map, min_dist=1, max_dist=3)


def part_2(heat_map: list[list[int]]) -> int:
    return path_len(heat_map, min_dist=4, max_dist=10)


if __name__ == '__main__':
    main()
