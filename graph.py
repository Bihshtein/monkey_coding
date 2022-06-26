from collections  import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_vertex: int, to_vertex : int):
        self.graph[from_vertex].append(to_vertex)

    @staticmethod
    def visit(visited_vertexes, vertex):
        visited_vertexes.append(vertex)
        print(visited_vertexes)
        return visited_vertexes

    def _dfs_util(self, origin_vertex: int, visited_vertexes: list):
        visited_vertexes = Graph.visit(visited_vertexes=visited_vertexes, vertex=origin_vertex)
        for neighbour in self.graph[origin_vertex]:
            if neighbour not in visited_vertexes:
                self._dfs_util(neighbour, visited_vertexes)
        return visited_vertexes

    def _bfs_util(self, to_visit_vertexes: list, visited_vertexes: list):
        next_to_visit_vertexes = []
        for neighbour in to_visit_vertexes:
            if neighbour not in visited_vertexes:
                visited_vertexes = Graph.visit(visited_vertexes=visited_vertexes, vertex=neighbour)
                next_to_visit_vertexes += self.graph[neighbour]
        if to_visit_vertexes:
            visited_vertexes = self._bfs_util(to_visit_vertexes=next_to_visit_vertexes, visited_vertexes=visited_vertexes)
        return visited_vertexes

    def dfs(self, vertex):
        return self._dfs_util(origin_vertex=vertex, visited_vertexes=[])

    def bfs(self, vertex):
        return self._bfs_util(to_visit_vertexes=[vertex], visited_vertexes=[])




