# Simple Tic-Tac-Toe Game (Beginner Friendly)

# Create the board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Function to print the board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check for a winner
def check_winner(player):
    # All winning combinations
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]

    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main game
current_player = "X"

for turn in range(9):  # Max 9 moves
    print_board()
    print(f"Player {current_player}, choose a position (1-9):")

    while True:
        try:
            move = int(input()) - 1   # convert to index 0-8

            if move < 0 or move > 8:
                print("Invalid position! Choose 1-9.")
            elif board[move] != " ":
                print("Spot already taken! Choose another.")
            else:
                break
        except:
            print("Enter a number from 1 to 9.")

    # Place the move
    board[move] = current_player

    # Check if the player wins
    if check_winner(current_player):
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

else:
    print_board()
    print("It's a draw! 🤝")

