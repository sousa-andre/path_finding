import time

from path_finding import Graph

LOOP_TIMES = 10000000

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

d_start_time = time.time()
for i in range(LOOP_TIMES):
    g.solve_char_with_dijkstra('A', 'H')
d_end_time = time.time()

a_start_time = time.time()
for i in range(LOOP_TIMES):
    g.solve_char_with_astar('A', 'H')
a_end_time = time.time()

print(f'Looped {LOOP_TIMES} times')
print(f'Dijkstra time: {d_end_time-d_start_time}s')
print(f'A* time: {a_end_time-a_start_time}s')
