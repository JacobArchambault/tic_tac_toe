from random import choice

def display(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""+-------+-------+-------+
|       |       |       |
|   {board[0]}   |   {board[1]}   |   {board[2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[3]}   |   {board[4]}   |   {board[5]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[6]}   |   {board[7]}   |   {board[8]}   |
|       |       |       |
+-------+-------+-------+""")


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

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            index = int(input("Enter your move: ")) - 1
            if board[index] not in ("O", "X"):
                board[index] = "O"
                return index, "O"
            else:
                print("That space is already occupied")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9")



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [x for x in board if x not in ("O", "X")]


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


def draw_move(board):
    # The function draws the computer's move and updates the board.
    available_fields = make_list_of_free_fields(board)
    computer_selection = choice(available_fields)
    index = computer_selection - 1
    board[index] = "X"
    return index, "X"

