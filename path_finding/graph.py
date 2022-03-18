

from .astar_solver import AStarSolver
from .dijkstra_solver import DijkstraSolver


A_ORD = ord('A')


class Graph:
    def __init__(self, size: int):
        self._size = size
        self._weights = [[0 for __ in range(size)] for _ in range(size)]

    @property
    def adjacency_matrix(self):
        return self._weights

    @property
    def adjacency_list(self):
        al = {}
        for row_idx, row in enumerate(self._weights):
            al[row_idx] = [(col_idx, weight,) for col_idx, weight in enumerate(row) if weight != 0]

        return al

    def add_edge(self, row: int, col: int, value: int):
        if len(self._weights) <= row:
            raise Exception("size matters")

        self._weights[row][col] = value
        self._weights[col][row] = value

    def add_edges(self, *edges):
        for edge in edges:
            self.add_edge(*edge)

    def add_edges_char(self, *edges):
        for edge in edges:
            self.add_edge(
                ord(edge[0]) - A_ORD,
                ord(edge[1]) - A_ORD,
                edge[2]
            )

    def solve_with_dijkstra(self, start, end):
        ds = DijkstraSolver(self._weights)
        ds.solution_table(start)
        return ds.back_track(end)

    def solve_char_with_dijkstra(self, start, end):
        return self.solve_with_dijkstra(ord(start) - A_ORD, ord(end) - A_ORD)

    def solve_with_astar(self, start, end):
        return AStarSolver(self.adjacency_list).solve(start, end)

    def solve_char_with_astar(self, start, end):
        return self.solve_with_astar(ord(start) - A_ORD, ord(end) - A_ORD)
