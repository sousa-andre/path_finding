from .dto import Node, Solution


class DijkstraSolver:
    def __init__(self, adjacency_matrix):
        self._weights = adjacency_matrix
        self._solved = []
        self._checked = []
        self._current = 0

    def _get_total_cost(self, col_idx):
        if self._solved[-2][col_idx].previous is None:
            return self._weights[self._current][col_idx]
        else:
            return self._weights[self._current][col_idx] + self._solved[-2][self._solved].value

    def _init_current(self, start):
        self._current = start
        self._checked.append(start)

    def _init_solver(self, start):
        self._solved.append([])
        for i in range(len(self._weights)):
            self._solved[0].append(Node(0 if i == start else float('inf'), None))
        self._init_current(start)

    def _next(self):
        tmp_min_weight = float('inf')
        tmp_min_idx = -1
        for idx, node in enumerate(self._solved[-1]):
            if tmp_min_weight > node.value and idx not in self._checked:
                tmp_min_weight = node.value
                tmp_min_idx = idx

        self._current = tmp_min_idx
        self._checked.append(self._current)

    def _sept_solver(self):
        self._solved.append([])

        for col_idx, weight in enumerate(self._weights[self._current]):
            prev_node = self._solved[-2][col_idx]
            current_node_array = self._solved[-1]

            curr_weight = weight + self._solved[-2][self._current].value if weight != 0 else weight

            if weight != 0 and prev_node.value > curr_weight:
                new_node = Node(curr_weight, self._current)

                current_node_array.append(new_node)
            else:
                current_node_array.append(prev_node)

        self._next()

    def solution_table(self, start):
        self._init_solver(start)

        while len(self._checked) < len(self._weights):
            self._sept_solver()
        return self._solved

    def back_track(self, end):
        path = []
        last_column = self._solved[-1]

        path.append(end)

        curr = last_column[end].previous
        while curr is not None:
            path.append(curr)
            curr = last_column[curr].previous

        return Solution(last_column[end].value, path[::-1])
