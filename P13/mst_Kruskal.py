class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u, v, weight) -> None:
        # new Nodes needs intialization
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # add the edge
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))


def kruskal_mst(graph):
    edges = []

    # extract the edges in array
    for node in graph.graph:
        for neighbor, weight in graph.graph[node]:
            edges.append((weight, node, neighbor))
    edges.sort()

    mst_edges = []

    # using set to remove duplicacy
    disjoint_sets = {node: node for node in graph.graph}
    print(disjoint_sets)
    for weight, u, v in edges:
        if disjoint_sets[u] != disjoint_sets[v]:
            mst_edges.append((u, v, weight))
            old_set, new_set = disjoint_sets[u], disjoint_sets[v]
            for node, set_id in disjoint_sets.items():
                if set_id == old_set:
                    disjoint_sets[node] = new_set

    return mst_edges


# Example usage
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)

mst_edges = kruskal_mst(graph)
print("Minimum Spanning Tree Edges are:", mst_edges)
