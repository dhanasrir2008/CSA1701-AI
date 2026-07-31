# Map Coloring using CSP (Backtracking)

# Define the map (graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store result
result = {}

# Check if color is valid
def is_valid(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

# Backtracking function
def solve(node_list, index):
    if index == len(node_list):
        return True
    
    node = node_list[index]
    
    for color in colors:
        if is_valid(node, color):
            result[node] = color
            
            if solve(node_list, index + 1):
                return True
            
            result[node] = None
    
    return False

# Main execution
nodes = list(graph.keys())

if solve(nodes, 0):
    print("Solution Found:")
    for node in result:
        print(node, "->", result[node])
else:
    print("No solution exists")
