# TODO: make a xox game
# ✅ || ❌
# TODO: make a function to fill the board ✅
# TODO: make a function to check the winner ✅
# TODO: make a function to check the draw ✅
# TODO: make a function to check the place is empty or not ✅
# TODO: make a function to ask the user to play ✅
# TODO: make a function to play the game ✅
# TODO: make a function to computer move ❌

# xox
import tabulate
import os
import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
play = True

# fill board returns xox_board changes board
def fill_board(value, place):  # place is between 1-9
    place -= 1
    row, col = divmod(place, 3)  # Use divmod for cleaner calculations
    board[row][col] = value
    return make_board(board)

# make board
def make_board(board):
    return tabulate.tabulate(board, tablefmt="rounded_grid")

# check the winner return the winner if there is a winner else return None
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

# check the draw return True if the board is full else return False
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# check the place is empty or not. return True if the place is empty else return False
def check_place_is_empty(board, place):
    place -= 1
    row, col = divmod(place, 3)
    return board[row][col] == ' '

# banner
def banner():
    print("=====================================")
    print("        Welcome to XOX Game!         ")
    print("=====================================")
    print("Here's how the board is structured:")
    print("\n  1 | 2 | 3 \n  --------- \n  4 | 5 | 6 \n  --------- \n  7 | 8 | 9 ")
    print("\nInstructions:")
    print("1. Player X and Player O take turns.")
    print("2. Choose a position (1-9) to place your mark.")
    print("3. The first player to align three marks wins!")
    print("4. If all positions are filled and no one wins, it's a draw.")
    print("\nLet the game begin!")

# play game
def play_game():
    global play
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    current_player = input("Choose your player (X or O): ").upper()
    user, computer = current_player, "O" if current_player == "X" else "X"

    if current_player not in ["X", "O"]:
        print("Invalid player choice. Restart the game.")
        return

    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{current_player}'s turn")
        print(make_board(board))
        try:
            if current_player == computer:
                place = computer_move(board, computer)
            else:
                place = int(input("Choose a position (1-9): "))
                if not 1 <= place <= 9 or not check_place_is_empty(board, place):
                    print("Invalid position or already occupied. Try again.")
                    continue

            fill_board(current_player, place)
            winner = check_winner(board)
            if winner:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{make_board(board)}\nCongratulations! {winner} wins!")
                play = False
            elif check_draw(board):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{make_board(board)}\nIt's a draw!")
                play = False
            else:
                current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# computer move. Returns best cell or random empty cell
def computer_move(gameState, player):
    opponent = "O" if player == "X" else "X"
    empty_cells = []
    best_attack_moves = []
    best_defend_moves = []
    corners = [1, 3, 7, 9]

    for row in range(3):
        for col in range(3):
            place = (row * 3) + col + 1
            if check_place_is_empty(gameState, place):
                empty_cells.append(place)
                for mark, target_list in [(player, best_attack_moves), (opponent, best_defend_moves)]:
                    board[row][col] = mark
                    if check_winner(board) == mark:
                        target_list.append(place)
                    board[row][col] = " "  # Reset

    # Prioritize moves
    if best_attack_moves:
        return random.choice(best_attack_moves)
    elif best_defend_moves:
        return random.choice(best_defend_moves)
    elif 5 in empty_cells:  # Center
        return 5
    elif any(c in empty_cells for c in corners):  # Corners
        return random.choice([c for c in corners if c in empty_cells])
    else:  # Random move
        return random.choice(empty_cells)

# start the game
play_game()
