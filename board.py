def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print(f"+-------+-------+-------+\n|       |       |       |\n|   {row[0]}   |   {row[1]}   |   {row[2]}   |\n|       |       |       |")
    print("+-------+-------+-------+")


board_dict = {1: (0, 0),
2: (0,1), 
3: (0,2),
4: (1,0),
5: (1,1),
6: (1,2),
7: (2,0),
8: (2,1),
9: (2,2)}

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move: "))
            index = board_dict[move]
            board[index[0]][index[1]] = "O"
            return
        except (ValueError, KeyError):
            print("Invalid input. Please enter a number between 1 and 9")



# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.
