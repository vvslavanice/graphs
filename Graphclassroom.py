class Vertex:
    def __init__(self, name):
        self.name = name
        self._neighbours = set()
        self._marked: bool = False

    def add_neighbour(self, new_newigbour: 'Vertex'):
        self._neighbours.add(new_newigbour)

    def get_name(self):
        return self.name

    def is_marked(self):
        return self._marked

    def mark(self):
        self._marked = True

    def __iter__(self):
        return iter(self._neighbours)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Vertex {self.name} with neighbours ' \
               f'{[n.name for n in self._neighbours]}'


class Graph:

    def __init__(self, edges):

        self._vertices = {name: Vertex(name) for name in edges.keys()}
        self.iters = 0

        for name, neighbours in edges.items():
            current_vertex = self._vertices[name]
            for neighbour in neighbours:
                current_vertex.add_neighbour(self._vertices[neighbour])


    def find_shortest_way(self, start: str, finish: str, path=[]):

        start_vertex = self._vertices[start]

        path = path + [start_vertex]

        if start == finish:
            return path

        if start not in self._vertices:
            return None

        shortest_path = None

        for neighbour in self._vertices[start]:
            self.iters += 1
            if neighbour not in path:

                sp = self.find_shortest_way(neighbour.get_name(), finish, path)

                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


edges = {'1': ['2', '3', '4'],
        '2': ['1', '5', '6'],
        '3': ['1'],
        '4': ['1', '7', '8'],
        '5': ['2'],
        '6': ['2', '14'],
        '7': ['4', '13'],
        '8': ['4'],
        '13': ['7', '14'],
        '14': ['6', '13']
        }

graph = Graph(edges)
print(graph.find_shortest_way('1', '6'))
print(graph.iters)
