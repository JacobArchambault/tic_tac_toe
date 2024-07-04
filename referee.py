import console_board

winning_moves_dictionary = {
    # pairs each index i for our list of spots on the board 
    # with tuples (j, k) representing each other pair of indices 
    # sufficient to win a game on a turn where the element at index i is selected
    0: ((1, 2), (3, 6), (4, 8)),
    1: ((0, 2), (4, 7)),
    2: ((0, 1), (5, 8), (4, 6)),
    3: ((4, 5), (0, 6)),
    4: ((3, 5), (1, 7), (0, 8), (2, 6)),
    5: ((3, 4), (2, 8)),
    6: ((7, 8), (0, 3), (2, 4)),
    7: ((6, 8), (1, 4)),
    8: ((6, 7), (2, 5), (0, 4))
}

def victory_for(index, sign, board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for pair in winning_moves_dictionary[index]:
        if board[pair[0]] == board[pair[1]] == sign: 
            console_board.display(board)
            print(f"{sign} wins!")
            exit()