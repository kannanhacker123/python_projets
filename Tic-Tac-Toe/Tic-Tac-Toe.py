# TODO: make a xox game
# ✅ || ❌
# TODO: make a function to fill the board ✅
# TODO: make a function to check the winner ✅
# TODO: make a function to check the draw ✅
# TODO: make a function to check the place is empty or not ✅
# TODO: make a function to ask the user to play ✅
# TODO: make a function to play the game ✅
# TODO: make a function to computer move ✅
# TODO: make a function to get valid input ✅
# TODO: make a function to clear the screen ✅
# TODO: make a function to print the banner ✅
# TODO: make a function to print the final statistics ✅
# TODO: make a function to choose the mode ✅

# xox
import tabulate
import os
import random
import copy

board_empty = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board = copy.deepcopy(board_empty)
play = True
play_count = 0
wins,loss,draw = 0,0,0
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
    global play
    if play_count == 0:
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
    else:
        table_headers = ["Wins", "Loss", "Draw"]
        table_data = [[wins, loss, draw]]
        print(tabulate.tabulate(table_data, headers=table_headers, tablefmt="rounded_grid"))
        replay = input("Do you want to play another game? (y/n): ").lower()
        if replay != "y":
            clear_screen()
            final_statistics()
            exit()
        
# game fun
def game():
    mode = choose_mode()
    if mode == 1:
        # player vs computer
        print("Player vs computer mode selected.")
        player_vs_computer()
    elif mode == 2:
        # player vs player
        print("Player vs Player mode selected.")
        print()
    elif mode == 3:
        # computer vs computer
        print("🤖 vs 🤖 - A fierce battle of artificial intelligence!")

    
    


# play game
def play_game():
    global play
    while play:
        clear_screen()
        banner() 
        game()

# computer move
def computer_move(gameState, player):
    """
    Determines the best move for the computer player in a Tic-Tac-Toe game.

    This function evaluates the current game state and selects a position 
    for the computer to place its mark ('X' or 'O') based on a set of 
    prioritized strategies:
    1. If there's a winning move, take it.
    2. Block the opponent's winning move if possible.
    3. If the center is available, take it.
    4. Choose a corner move if available.
    5. Select a random empty position if no other priorities are met.

    Args:
        gameState (list of list of str): The current state of the game board.
        player (str): The computer's mark ('X' or 'O').

    Returns:
        int: The position (1-9) where the computer should make a move.
    """
    opponent = "O" if player == "X" else "X"
    empty_cells = []
    best_attack_moves = []
    best_defend_moves = []
    corners = [1, 3, 7, 9]

    # Use a copy of the board for simulating moves
    temp_board = copy.deepcopy(gameState)

    for row in range(3):
        for col in range(3):
            place = (row * 3) + col + 1
            if check_place_is_empty(temp_board, place):
                empty_cells.append(place)
                for mark, target_list in [(player, best_attack_moves), (opponent, best_defend_moves)]:
                    temp_board[row][col] = mark
                    if check_winner(temp_board) == mark:
                        target_list.append(place)
                    temp_board[row][col] = " "  # Reset
    # if 
    # Prioritize moves
    if best_attack_moves: # 1st priority is attack  
        return random.choice(best_attack_moves) 
    elif best_defend_moves:# 2nd priority is defend
        return random.choice(best_defend_moves) 
    elif 5 in empty_cells:  # 3rd priority is corner
        return 5
    elif any(c in empty_cells for c in corners):  # 4th priority is corner
        return random.choice([c for c in corners if c in empty_cells])
    else:  # Random move for last resort
        return random.choice(empty_cells)


# player vs computer function
def player_vs_computer():
    current_player = input("Choose your player (X or O): ").upper()
    global play,play_count,board,wins,loss,draw
    user, computer = current_player, "O" if current_player == "X" else "X"

    if current_player not in ["X", "O"]:
        print("Invalid player choice. Restart the game.")
        return

    while play:
        clear_screen()
        print(f"\n{current_player}'s turn")
        print(make_board(board))
        try:
            if current_player == computer:
                place = computer_move(board, computer)
            else:
                place = get_valid_input()
                if place == None:
                    clear_screen()
                    final_statistics()
                    exit()
                elif  type(place) == str:
                    print(place)
                    continue
            fill_board(current_player, place)
            winner = check_winner(board)
            if winner:
                clear_screen()
                print(f"{make_board(board)}\nCongratulations! {winner} wins!")
                
                play_count += 1 
                board = copy.deepcopy(board_empty)
                if winner == user:
                    print("🎉 Congratulations! You won!")
                    print("🤔 Did you just outsmart a computer? That's impressive!")
                    print("Don't get too cocky, though. The machine is learning...\n")
                    wins += 1
                else:
                    loss += 1
                    print("💻 The computer wins this round!")
                    print("🤖 I told you, resistance is futile!")
                    print("Better luck next time, human.\n")
                input("Press Enter to continue...")
                break
            elif check_draw(board):
                clear_screen()
                print(f"{make_board(board)}\nIt's a draw!")
                print("😐 It's a draw!")
                print("No winners here, just two equally stubborn opponents.")
                print("Try again—maybe you'll outwit me this time!")
                play_count += 1
                board = copy.deepcopy(board_empty)
                draw += 1
                input("Press Enter to continue...")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# vaild input
def get_valid_input():
    while True:
        place = input("Choose a position (1-9 or 'q' to quit): ").lower()
        if place == "q":
            global play
            play = False
            return  None# Break out of the loop or exit gracefully
        try:
            place = int(place)
            if 1 <= place <= 9 and check_place_is_empty(board, place):
                return place
            else:
                return "Invalid or occupied position. Try again."
        except ValueError:
            return "Enter a valid number between 1 and 9."


# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# final_statistics
def final_statistics():
    print("\nFinal Statistics:")
    table_headers = ["Wins", "Losses", "Draws"]
    table_data = [[wins, loss, draw]]
    print(tabulate.tabulate(table_data, headers=table_headers, tablefmt="rounded_grid"))

# choose mode funtion returns the mode = 1,2,3
def choose_mode():
    while True:
        print("Select game mode:")
        print("1. Player vs Computer")
        print("2. Player vs Player")
        print("3. Computer vs Computer")
        mode = input("Enter your choice (1-3): ").strip()
        if mode in ["1", "2", "3"]:
            return int(mode)
        print("Invalid choice. Please try again.")

# start the game
play_game()
