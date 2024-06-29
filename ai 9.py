from itertools import permutations

def calculate_total_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Returning to the start point
    return total_distance

def travelling_salesman_problem(graph):
    cities = list(graph.keys())
    min_path = None
    min_distance = float('inf')
    
    for perm in permutations(cities):
        current_distance = calculate_total_distance(graph, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
            
    return min_path, min_distance

# Example usage
if __name__ == "__main__":
    # Representation of the graph as an adjacency matrix
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }

    path, distance = travelling_salesman_problem(graph)
    print(f"Shortest path: {' -> '.join(path)}")
    print(f"Total distance: {distance}")
