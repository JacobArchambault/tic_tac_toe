winning_moves_dictionary = {
    # pairs each index with the tuples required to complete a row with it 
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
    pairs_to_check = winning_moves_dictionary[index]
    wins = False
    for pair in pairs_to_check:
        if board[pair[0]] == board[pair[1]] == sign: 
            wins = True
            break
    return wins, sign