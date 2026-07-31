def dfs_recursive(graph, node, visited, result):
    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)


def dfs(graph, start):
    visited = set()
    result = []
    dfs_recursive(graph, start, visited, result)
    return result


# Graph input
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

start_node = 'A'

result = dfs(graph, start_node)

print("DFS Traversal:", result)
