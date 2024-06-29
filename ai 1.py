import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.size = int(len(board) ** 0.5)

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def find_zero(self):
        return self.board.index(0)

    def swap(self, i, j):
        new_board = list(self.board)
        new_board[i], new_board[j] = new_board[j], new_board[i]
        return PuzzleState(tuple(new_board), self.moves + 1, self)

    def neighbors(self):
        zero = self.find_zero()
        row, col = divmod(zero, self.size)
        swaps = []
        if row > 0: swaps.append(zero - self.size)  # up
        if row < self.size - 1: swaps.append(zero + self.size)  # down
        if col > 0: swaps.append(zero - 1)  # left
        if col < self.size - 1: swaps.append(zero + 1)  # right
        return [self.swap(zero, swap) for swap in swaps]

    def manhattan(self):
        distance = 0
        for i, tile in enumerate(self.board):
            if tile == 0:
                continue
            goal_pos = tile - 1
            current_row, current_col = divmod(i, self.size)
            goal_row, goal_col = divmod(goal_pos, self.size)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def heuristic(self):
        return self.moves + self.manhattan()

    def is_goal(self):
        return self.board == tuple(range(1, self.size * self.size)) + (0,)

    def path(self):
        state = self
        result = []
        while state:
            result.append(state.board)
            state = state.previous
        return result[::-1]

def solve_puzzle(initial_board):
    start = PuzzleState(initial_board)
    frontier = []
    heapq.heappush(frontier, start)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)

        if current.is_goal():
            return current.path()

        explored.add(current.board)

        for neighbor in current.neighbors():
            if neighbor.board not in explored:
                heapq.heappush(frontier, neighbor)

    return None

# Example usage:
initial_board = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Solved state
initial_board_scrambled = (1, 2, 3, 4, 5, 6, 0, 7, 8)  # Example scrambled state

solution = solve_puzzle(initial_board_scrambled)
for step in solution:
    print(step)
