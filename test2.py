from pprint import pprint

from path_finding import Graph

g = Graph(6)
g.add_edges(
    [
        0, 1, 4
    ],
    [
        0, 3, 2
    ],
    [
        1, 2, 3
    ],
    [
        1, 4, 3
    ],
    [
        2, 5, 2
    ],
    [
        3, 4, 3
    ],
    [
        4, 5, 1
    ]
)

pprint(g.adjacency_list)
pprint(g.solve_with_dijkstra(0, 5))
