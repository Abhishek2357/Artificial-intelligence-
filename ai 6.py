from collections import deque

# Directions for moving in the grid (left, right, up, down)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if a state is valid
def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

# Function to check if the grid is fully cleaned
def is_clean(grid):
    for row in grid:
        if 'D' in row:
            return False
    return True

# Function to perform the BFS
def bfs(start, grid):
    queue = deque([start])
    visited = set()
    visited.add((start[0], start[1], tuple(tuple(row) for row in grid)))
    parent = {((start[0], start[1], tuple(tuple(row) for row in grid))): None}
    
    while queue:
        x, y, grid = queue.popleft()
        
        if is_clean(grid):
            path = []
            state = (x, y, tuple(tuple(row) for row in grid))
            while state:
                path.append(state)
                state = parent[state]
            path.reverse()
            return path
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                new_grid = [list(row) for row in grid]
                if new_grid[nx][ny] == 'D':
                    new_grid[nx][ny] = 'C'
                new_state = (nx, ny, tuple(tuple(row) for row in new_grid))
                if new_state not in visited:
                    queue.append(new_state)
                    visited.add(new_state)
                    parent[new_state] = (x, y, tuple(tuple(row) for row in grid))
                    
    return None

# Function to print the solution path
def print_solution(path):
    for state in path:
        x, y, grid = state
        print(f"Vacuum Cleaner at: ({x}, {y})")
        for row in grid:
            print(" ".join(row))
        print()

# Example grid and starting position
# 'D' represents dirty and 'C' represents clean
grid = [
    ['D', 'D'],
    ['D', 'D']
]

start_position = (0, 0)  # Starting at top-left corner

# Clean the starting position if it's dirty
if grid[start_position[0]][start_position[1]] == 'D':
    grid[start_position[0]][start_position[1]] = 'C'

solution = bfs(start_position, grid)
if solution:
    print_solution(solution)
else:
    print("No solution found")
