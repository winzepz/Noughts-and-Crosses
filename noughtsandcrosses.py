import random
import os.path
import json
random.seed()

def draw_board(board):
    """This fucntion Draw Board"""
    # the board is drawn.
    for row in range(3):
        print("-----------")
        for col in range(3):
            print(f"| {board[row][col]}", end="")
        print('|')
    print("-----------")


def welcome(board):
    """This is the welcome fucntion"""
    print('Welcome to the "Unbeatable Noughts and Crosses" game')
    print(("This program is created By Darwin Paudel"))
    draw_board(board)
    print("When prompted, enter the number corresponding to enter your selection.")


def initialise_board(board):
    """This function Initialize the Board with empty space"""
    # Setting all elements of the board to empty spaces ' '
    for m in range(3):
        for n in range(3):
            board[m][n] = ' '
    return board


def get_player_move(board):
    """This function recieve players input"""
    # Asking the user for slot selection.
    while True:
        available_moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    available_moves.append(str(row * 3 + col + 1))
        print("Remaining available moves:", ", ".join(available_moves))
        player_move = input("Choose your slot: ")
        if player_move.isdigit() and int(player_move) in range(1, 10):
            player_move = int(player_move) - 1
            row = player_move // 3
            col = player_move % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print("Slot is already occupied! choose a different slot.")
        else:
            print("Invalid input!!! Enter a number among", available_moves, ".")


def choose_computer_move(board):
    """This function generate computer move"""
    # Check if the computer can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_for_win(board, 'O') == True:
                    return row, col
                else:
                    board[row][col] = ' '

    # Check if the player can win in the next move or not to block player.
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_for_win(board, 'X') == True:
                    board[row][col] = 'O'
                    return row, col
                else:
                    board[row][col] = ' '

    # If both case are not possible, it will choose a random empty slot
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col



def check_for_win(board, mark):
    """This function check who won the game"""
    # it Checks if either the player or the computer has won
    # and Return true if someone won, otherwise false
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    """This function check for draw case"""
    # check for any possible moves and return True if not.
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True


def play_game(board):
    """This function play the game"""
    # start game
    initialise_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations You Won Against Computer")
            return 1
        if check_for_draw(board):
            print("Its Draw!!")
            return 0
        row, col = choose_computer_move(board)
        print("Computer selects its slot.")
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer Won! I told you the computer is unbeatable.")
            return -1
        if check_for_draw(board):
            print("Its Draw!!")
            return 0

def menu():
    """The function has main menu of game"""
    # print the menu option
    while True:
        choice = input("""Enter one of the following options:
        1 - Play the game
        2 - Save your score in the leaderboard
        3 - Load and display the leaderboard
        q - End the program
        1, 2, 3 or q? """)
        options = ['1', '2', '3', 'q', 'Q']
        if choice not in options:
            print("Invalid Choice!!")
            continue
        else:
            break
    return choice

def load_scores():
    """This function load score of leaderboard"""
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = {}
    return leaderboard


def save_score(score):
    """This function save the score obtain by player"""
    player_name = input("What's your sweet name?: ")
    leaderboard = load_scores()
    leaderboard[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaderboard, file)


def display_leaderboard(leaders):
    """This function display the leaderboard"""
    print("Name: Score")
    for name, score in leaders.items():
        print(f"{name}: {score}")
