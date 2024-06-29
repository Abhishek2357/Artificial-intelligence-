def is_valid(graph, colors, node, color):
    """Check if it's valid to color the node with the given color."""
    for neighbor in graph[node]:
        if neighbor in colors and colors[neighbor] == color:
            return False
    return True

def csp_map_coloring(graph, colors, node, color_map):
    """Backtracking algorithm to solve the Map Coloring CSP."""
    if node == len(graph):
        return True
    
    # Get the next node to color
    nodes = list(graph.keys())
    current_node = nodes[node]
    
    for color in color_map:
        if is_valid(graph, colors, current_node, color):
            colors[current_node] = color
            if csp_map_coloring(graph, colors, node + 1, color_map):
                return True
            colors[current_node] = None  # Backtrack
    
    return False

def solve_map_coloring(graph, color_map):
    """Solve the Map Coloring problem using backtracking."""
    colors = {node: None for node in graph}
    if csp_map_coloring(graph, colors, 0, color_map):
        return colors
    else:
        return None

# Example usage
if __name__ == "__main__":
    # Graph representation of regions as an adjacency list
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['A', 'B', 'C']
    }

    # List of available colors
    color_map = ['Red', 'Green', 'Blue']

    result = solve_map_coloring(graph, color_map)
    if result:
        print("Solution found:")
        for region, color in result.items():
            print(f"Region {region}: {color}")
    else:
        print("No solution found")
