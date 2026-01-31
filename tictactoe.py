# Tic-Tac-Toe in Python

# Welcomes player and asks which marker player 1 will be
def player_input():
    print("Welcome to Tic-Tac-Toe!")
    valid_choices = ['X', 'O']
    player_1 = 'wrong'
    while player_1 not in valid_choices:
        player_1 = input("Player 1, do you want to be X or O? ").upper()

        if player_1 not in valid_choices:
            print("Not a valid choice!")

    player_2 = 'wrong'
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    return (player_1, player_2)

# Asks player if they're ready to start the game

def starting(p1, p2):
    valid_choices = ['yes', 'no']
    play = 'wrong'
    while play not in valid_choices:
        if p1 == 'X':
            print("Player 1 will go first")
        else:
            print("Player 2 will go first")
        play = input("Are you ready to play? Answer 'yes' or 'no': ").lower()

        if play not in valid_choices:
            print("Not a valid choice!")
    return True if play == 'yes' else False

# Asks current player the next position

def position(current_player):
    valid_positions = list(range(1, 10))
    user_position = 'wrong'
    while user_position not in valid_positions:
        try:
            user_position = int(
                input(f"Player {current_player}, Choose your next position (1-9): "))
        except:
            print("Not a valid position!")
    return user_position


def display_game(board):
    print('\n'*100)
    print("   |   |   \n" + " " + board[1] + " " + "| " + board[2] + " | " + board[3] + " \n" + "   |   |   \n" + "-----------\n" + "   |   |   \n" + " " + board[4] + " " + "| " +
          board[5] + " | " + board[6] + " \n" + "   |   |   \n" + "-----------\n" + "   |   |   \n" + " " + board[7] + " " + "| " + board[8] + " | " + board[9] + " \n" + "   |   |   \n")


def place_marker(board, marker, position):
    board[position] = marker
    return board

# Check for all possible game win matches

def checkwin(board, current_player):
    return (
    (current_player in board[1] and current_player in board[2] and current_player in board[3]) or
    (current_player in board[4] and current_player in board[5] and current_player in board[6]) or
    (current_player in board[7] and current_player in board[8] and current_player in board[9]) or
    (current_player in board[1] and current_player in board[4] and current_player in board[7]) or
    (current_player in board[2] and current_player in board[5] and current_player in board[8]) or
    (current_player in board[3] and current_player in board[6] and current_player in board[9]) or
    (current_player in board[1] and current_player in board[5] and current_player in board[9]) or
    (current_player in board[3] and current_player in board[5] and current_player in board[7])
)

# Ask to replay the game

def replay():
    valid_answers = ['yes', 'no']
    answer = 'wrong'
    while answer not in valid_answers:
        answer = input("Do you want to play again? Type 'yes' or 'no': ").lower()

        if answer not in valid_answers:
            print("Not a valid answer!")
    if answer == 'yes':
        return True
    else:
        return False

# Main function

def game():
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    current_player = 'X'
    game_on = starting(player1_marker, player2_marker)
    if game_on:
        display_game(board)
    while game_on:
        marker_place = position(current_player)
        if board[marker_place] == ' ':
            updated_board = place_marker(board, current_player, marker_place)
            display_game(updated_board)
            if checkwin(board, current_player):
                print(f"Player {current_player} wins!")
                game_on = False
                break
            if ' ' not in board[1:]:
                print("It's a tie!")
                game_on = False
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again")
    if not game_on and not ' ' in board:
        play = replay()
        if play:
            game()
        else:
            print("Until next time!")

game()
