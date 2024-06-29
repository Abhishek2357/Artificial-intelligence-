from collections import deque

# A utility function to check if a state is valid
def is_valid(state):
    m, c, boat = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m < c and m > 0) or ((3 - m) < (3 - c) and (3 - m) > 0):
        return False
    return True

# Function to perform the BFS
def bfs(start, goal):
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    while queue:
        state = queue.popleft()
        
        if state == goal:
            path = []
            while state:
                path.append(state)
                state = parent[state]
            path.reverse()
            return path
        
        m, c, boat = state
        # Possible moves
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            if boat == 1:
                new_state = (m - move[0], c - move[1], 0)
            else:
                new_state = (m + move[0], c + move[1], 1)
                
            if is_valid(new_state) and new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                parent[new_state] = state
    
    return None

# Function to print the solution path
def print_solution(path):
    for state in path:
        m, c, boat = state
        boat_side = 'left' if boat == 1 else 'right'
        print(f"Missionaries: {m}, Cannibals: {c}, Boat: {boat_side}")

# Initial state: (3, 3, 1) -> 3 missionaries, 3 cannibals, boat on the left
# Goal state: (0, 0, 0) -> 0 missionaries, 0 cannibals, boat on the right
start_state = (3, 3, 1)
goal_state = (0, 0, 0)

solution = bfs(start_state, goal_state)
if solution:
    print_solution(solution)
else:
    print("No solution found")
