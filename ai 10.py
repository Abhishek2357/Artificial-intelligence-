import heapq

def heuristic(a, b):
    """Calculate the heuristic (Euclidean distance) between point a and point b."""
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def a_star(graph, start, goal):
    """Find the shortest path from start to goal using the A* algorithm."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# Example usage
if __name__ == "__main__":
    # Graph represented as an adjacency list with distances
    graph = {
        (0, 0): {(1, 1): 1.5, (1, 0): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(1, 0): 1, (0, 0): 1.5, (2, 2): 1.5},
        (2, 2): {(1, 1): 1.5}
    }

    start = (0, 0)
    goal = (2, 2)
    path = a_star(graph, start, goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found")
