class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if self.adj_list.get(vertex1) is not None and self.adj_list.get(vertex2) is not None:
            self.adj_list.get(vertex1).append(vertex2)
            self.adj_list.get(vertex2).append(vertex1)
            return True
        return False
    
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')

my_graph.add_edge('A', 'B')

my_graph.print_graph()