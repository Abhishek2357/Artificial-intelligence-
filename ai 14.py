import math

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the player has won."""
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Check if the game is a draw."""
    return all(all(cell != " " for cell in row) for row in board)

def minimax(board, depth, alpha, beta, is_maximizing):
    """Minimax algorithm with alpha-beta pruning."""
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_draw(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    """Find the best move for the AI player using alpha-beta pruning."""
    best_score = float('-inf')
    move = None
    alpha = float('-inf')
    beta = float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, alpha, beta, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
                alpha = max(alpha, score)
    return move

def tic_tac_toe():
    """Play a game of Tic Tac Toe against an AI with alpha-beta pruning."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"
    current_player = human
    
    while True:
        print_board(board)
        if current_player == human:
            while True:
                try:
                    move = int(input(f"Player {human}, enter your move (1-9): ")) - 1
                    if move < 0 or move >= 9:
                        raise ValueError
                    row, col = divmod(move, 3)
                    if board[row][col] == " ":
                        board[row][col] = human
                        break
                    else:
                        print("This cell is already occupied. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number between 1 and 9.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = ai
                print(f"AI ({ai}) chose position {move[0] * 3 + move[1] + 1}")
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = ai if current_player == human else human

if __name__ == "__main__":
    tic_tac_toe()
