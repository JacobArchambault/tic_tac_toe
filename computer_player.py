from random import choice

def draw_move(board):
    # The function performs the computer's move 
    # and updates the board.
    index = choice([x for x in board if x not in ("O", "X")]) - 1
    board[index] = "X"
    return index, "X"

