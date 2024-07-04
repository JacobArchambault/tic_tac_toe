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
    wins, sign = referee.victory_for(index, sign, game_board)
    if wins:
        console_board.display(game_board)
        print(f"{sign} wins!")
        break
    console_board.display(game_board)
    index, sign = computer_player.draw_move(game_board)
    wins, sign = referee.victory_for(index, sign, game_board)
    if wins:
        console_board.display(game_board)
        print(f"{sign} wins!")
        break