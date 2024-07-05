import console_board
import console_player    
import computer_player
import referee
import start_menu

players = start_menu.select_players()
player_one_function = computer_player.enter_move if players == 1 else console_player.enter_move
game_board = [1,2,3,
    4,5,6,
    7,8,9]
turn = 1
while turn <= 9:
    console_board.display(game_board)
    index, sign = player_one_function(game_board, "X") if turn % 2 else console_player.enter_move(game_board)
    referee.victory_for(index, sign, game_board)
    turn += 1
console_board.display(game_board)
print("It's a draw!")