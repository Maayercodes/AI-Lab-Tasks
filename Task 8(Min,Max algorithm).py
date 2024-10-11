#  Code of "Min Max Algorithm
import math
def check_winner(board):
    """Check if there is a winner on the board."""
    winning_combinations = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for combo in winning_combinations:
        if combo[0] == combo[1] == combo[2] and combo[0] != '_':
            return combo[0]  
    return None  
def is_draw(board):
    return all(cell != '_' for row in board for cell in row)
def minmax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1 
    elif winner == 'O':
        return -1  
    elif is_draw(board):
        return 0 
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':  
                    board[i][j] = 'X' 
                    score = minmax(board, depth + 1, False)
                    board[i][j] = '_' 
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O' 
                    score = minmax(board, depth + 1, True)
                    board[i][j] = '_' 
                    best_score = min(best_score, score)
        return best_score
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_': 
                board[i][j] = 'X'
                move_score = minmax(board, 0, False)
                board[i][j] = '_'
                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)
    return best_move
board = [
    ['X', 'O', 'X'],
    ['_', 'O', '_'],
    ['_', '_', '_']
]
best_move = find_best_move(board)
print("Best move for X is:", best_move)
