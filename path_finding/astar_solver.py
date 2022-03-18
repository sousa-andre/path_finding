from .dto import Solution


class AStarSolver:
    def __init__(self, adjacency_list):
        self._adjacency_list = adjacency_list

    @staticmethod
    def _heuristic(n):
        return 1

    def _get_neighbors(self, v):
        return self._adjacency_list[v]

    def _find_weight(self, frm, to):
        for v in self._adjacency_list[frm]:
            if v[0] == to:
                return v[1]

    def calculate_cost(self, path):
        s = 0
        for i in range(len(path)-1):
            s += self._find_weight(path[i], path[i+1])
        return s

    def solve(self, start_node, stop_node):
        # Source: https://stackabuse.com/basic-ai-concepts-a-search-algorithm/
        # Author: Vladimir Batoćanin
        open_list = {start_node}
        closed_list = set([])

        g = {start_node: 0}
        parents = {start_node: start_node}

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n is None or g[v] + self._heuristic(v) < g[n] + self._heuristic(n):
                    n = v

            if n is None:
                return None
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                return Solution(self.calculate_cost(reconst_path), reconst_path)
            for (m, weight) in self._get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)
        return None