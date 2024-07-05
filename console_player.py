def enter_move(board, sign="O"):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            index = int(input("Enter your move: ")) - 1
            if board[index] not in ("O", "X"):
                board[index] = sign
                return index, sign
            else:
                print("That space is already occupied")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9")