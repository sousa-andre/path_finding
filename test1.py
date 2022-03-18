from pprint import pprint

from path_finding import Graph


g = Graph(8)
g.add_edges_char(
    [
        'A', 'B', 5
    ],
    [
        'A', 'F', 3
    ],
    [
        'B', 'G', 3
    ],
    [
        'B', 'C', 2
    ],
    [
        'C', 'H', 10
    ],
    [
        'H', 'G', 2
    ],
    [
        'G', 'F', 7
    ],
    [
        'F', 'E', 8
    ],
    [
        'E', 'D', 3
    ],
    [
        'D', 'C', 6
    ],
    [
        'H', 'E', 5
    ]
)


pprint(g.adjacency_list)
pprint(g.solve_char_with_dijkstra('A', 'H'))
pprint(g.solve_char_with_astar('A', 'H'))
