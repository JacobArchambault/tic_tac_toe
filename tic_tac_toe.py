import board    
game_board = [1,2,3,
    4,"X",6,
    7,8,9]
board.display(game_board)
index, sign = board.enter_move(game_board)
wins = board.victory_for(index, sign)
board.display(game_board)
# available_moves = make_list_of_free_fields(game_board)

# display board
# prompt user to make first move
# validate input
    # error message, reprompt user
# update board
# check if there's a winner
# computer move
#