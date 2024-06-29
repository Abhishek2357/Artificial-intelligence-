from collections import deque

# Function to print the solution path
def print_solution_path(path):
    for state in path:
        print(f"Jug1: {state[0]} liters, Jug2: {state[1]} liters")
    print()

# Function to perform the BFS
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Initial state (0, 0) with both jugs empty
    start = (0, 0)
    
    # Queue for BFS
    queue = deque([start])
    
    # Set to keep track of visited states
    visited = set()
    visited.add(start)
    
    # Dictionary to store the path
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        # If we reach the target amount in either jug, print the solution path
        if current[0] == target or current[1] == target:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print_solution_path(path)
            return
        
        # Possible states from the current state
        possible_states = [
            (jug1_capacity, current[1]),  # Fill Jug1
            (current[0], jug2_capacity),  # Fill Jug2
            (0, current[1]),              # Empty Jug1
            (current[0], 0),              # Empty Jug2
            (max(current[0] - (jug2_capacity - current[1]), 0), 
             min(current[1] + current[0], jug2_capacity)),  # Pour Jug1 -> Jug2
            (min(current[0] + current[1], jug1_capacity), 
             max(current[1] - (jug1_capacity - current[0]), 0))  # Pour Jug2 -> Jug1
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = current

    print("No solution found")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_bfs(jug1_capacity, jug2_capacity, target)
