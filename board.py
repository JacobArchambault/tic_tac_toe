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

