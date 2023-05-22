# Tic-Tac-Toe Game

def print_board(board):
    """Prints the current state of the board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner"""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def play_game():
    """Plays a game of Tic-Tac-Toe"""
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    winner = None

    while not winner:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Update the board
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Check for a winner
        winner = check_winner(board)

        # Switch players
        current_player = "O" if current_player == "X" else "X"

    # Print the final board
    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()
