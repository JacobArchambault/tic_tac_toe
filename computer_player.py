from random import choice

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [x for x in board if x not in ("O", "X")]

def draw_move(board):
    # The function draws the computer's move and updates the board.
    available_fields = make_list_of_free_fields(board)
    computer_selection = choice(available_fields)
    index = computer_selection - 1
    board[index] = "X"
    return index, "X"

