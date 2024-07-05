from random import choice

def enter_move(board, sign):
    # The function performs the computer's move 
    # and updates the board.
    index = choice([x for x in board if x not in ("O", "X")]) - 1
    board[index] = sign
    return index, sign

