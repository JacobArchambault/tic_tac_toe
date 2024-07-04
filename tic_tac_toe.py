import console_board
import console_player    
import computer_player
import referee

game_board = [1,2,3,
    4,"X",6,
    7,8,9]
while True:
    console_board.display(game_board)
    index, sign = console_player.enter_move(game_board)
    referee.victory_for(index, sign, game_board)
    console_board.display(game_board)
    index, sign = computer_player.draw_move(game_board)
    referee.victory_for(index, sign, game_board)