# Triple A-level game here, folks. Activision Blizzard, Bethesda, Valve... hit me up, let's make a deal.

# The board!
board = ["-", "-", "-", 
        "-", "-", "-", 
        "-", "-", "-"]

#Switch to determine if the game is still going
game_still_going = True

#Is there a winner?
winner = None

#Current player "X" or "O"
current_player = "X"

#Display the board!
def display_board():
    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play the game, duh.
def play_game():
    print("|||||||||||")
    print("Game started!")
    print("|||||||||||")
    display_board()

    #While the game is still going... obviously...
    while game_still_going:

        #handle a single turn of whichever player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()
        
        # Flip to the other player
        flip_player()

        if winner == "X" or winner == "O":
            print(winner + "won!")
        elif winner == None:
            print("Tie!")
        



def handle_turn(player):
    position = input("Choose a position from 1 - 9: ")
    position = int(position) - 1
    board[position] = "X"
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner()
    elif column_winner: 
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    

    return

def check_rows():
    global game_still_going
    # Check if any of the rows have the same value
    row_1 = board[0] == board[1] == [2] != "-"
    row_2 = board[3] == board[4] == [5] != "-"
    row_3 = board[6] == board[7] == [8] != "-"
    # If any row has a match, flag as win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2: 
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == [6] != "-"
    column_2 = board[1] == board[4] == [7] != "-"
    column_3 = board[2] == board[5] == [8] != "-"
    # If any row has a match, flag as win
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2: 
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == [8] != "-"
    diagonal_2 = board[2] == board[4] == [6] != "-"
    # If any row has a match, flag as win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2: 
        return board[2]
    return

def check_if_tie():
    return

def flip_player():
    return

play_game()