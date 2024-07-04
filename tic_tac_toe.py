import board    
import computer_player

game_board = [1,2,3,
    4,"X",6,
    7,8,9]
while True:
    board.display(game_board)
    index, sign = board.enter_move(game_board)
    wins, sign = board.victory_for(index, sign, game_board)
    if wins:
        board.display(game_board)
        print(f"{sign} wins!")
        break
    board.display(game_board)
    index, sign = computer_player.draw_move(game_board)
    wins, sign = board.victory_for(index, sign, game_board)
    if wins:
        board.display(game_board)
        print(f"{sign} wins!")
        break