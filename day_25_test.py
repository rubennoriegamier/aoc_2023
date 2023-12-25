from unittest import TestCase, main

import networkx as nx

from day_25 import components_graph, part_1


class TestDay25(TestCase):
    _components: nx.Graph

    def setUp(self):
        self._components = components_graph(['jqt: rhn xhk nvd',
                                             'rsh: frs pzl lsr',
                                             'xhk: hfx',
                                             'cmg: qnr nvd lhk bvb',
                                             'rhn: xhk bvb hfx',
                                             'bvb: xhk hfx',
                                             'pzl: lsr hfx nvd',
                                             'qnr: nvd',
                                             'ntq: jqt hfx bvb xhk',
                                             'nvd: lhk',
                                             'lsr: lhk',
                                             'rzs: qnr cmg lsr rsh',
                                             'frs: qnr lhk lsr'])

    def test_part_1(self):
        self.assertEqual(part_1(self._components), 54)


if __name__ == '__main__':
    main()
