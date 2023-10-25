def DFS(graph, start_node):
    stack = []
    visited = set()
    traversal = []

    stack.append(start_node)
    visited.add(start_node)

    while stack:
        current_node = stack.pop()
        traversal.append(current_node)

        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
                visited.add(adjacent_node)

    return traversal


def BFS(graph, start_node):
    queue = []
    visited = set()
    traversal = []

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        traversal.append(current_node)

        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
                visited.add(adjacent_node)

    return traversal


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A'],
    'D': ['A', 'H'],
    'E': ['B', 'F', 'G'],
    'F': ['E', 'G'],
    'G': ['E', 'F'],
    'H': ['D', 'I'],
    'I': ['H']
}

DFS_traversal = DFS(graph, 'A')
print("The DFS Traversal from Node A: ", DFS_traversal)
BFS_traversal = BFS(graph, 'A')
print("The BFS Traversal from Node A:", BFS_traversal)
