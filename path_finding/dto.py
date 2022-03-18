# DTOs
class Node:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous

    def __repr__(self):
        return f'Node({self.value}, {self.previous})'


class Solution:
    def __init__(self, cost, path):
        self.cost = cost
        self.path = path

    def __repr__(self):
        return f'Solution({self.cost}, {self.path})'