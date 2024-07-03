from board import display_board, enter_move, make_list_of_free_fields

game_board = [[1,2,3],
    [4,"X",6],
    [7,8,9]]
display_board(game_board)
enter_move(game_board)
display_board(game_board)
make_list_of_free_fields(game_board)