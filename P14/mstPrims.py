import heapq


def prim_mst(graph):
    mincost = 0
    mst_edges = []
    start_node = next(iter(graph))  # Start from the first node in the graph
    min_heap = [(0, start_node, None)]  # (weight, current_node, parent_node)

    visited = set()

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst_edges.append((parent, node))
                mincost += weight
            for neighbor, edge_weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mincost, mst_edges


# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

mincost, mst_edges = prim_mst(graph)
print("For the graph:", graph)
print("Cost of MST using prims algo:", mincost)
print("Edges of MST:", mst_edges)
