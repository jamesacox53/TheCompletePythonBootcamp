def display_board(board):
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print(f'---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(f'---+---+---')
    print(f' {board[0]} | {board[1]} | {board[2]} ')

def choose_player_markers():
    p1_choice = ''

    while p1_choice not in ['X', 'O']:
        p1_choice = input('Player 1 do you want to be X or O? ').strip().upper()

        if p1_choice not in ['X', 'O']:
            print("Sorry, you can't be that.")

    if p1_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    board[position - 1] = marker

def win_check(board, marker):
    won_top_row = marker == board[6] == board[7] == board[8]
    won_middle_row = marker == board[3] == board[4] == board[5]
    won_bottom_row = marker == board[0] == board[1] == board[2]
    
    won_left_col = marker == board[6] == board[3] == board[0]
    won_mid_col = marker == board[7] == board[4] == board[1]
    won_right_col = marker == board[8] == board[5] == board[2]

    won_left_diag = marker == board[0] == board[4] == board[8]
    won_right_diag = marker == board[6] == board[4] == board[2]

    won_row = won_top_row or won_middle_row or won_bottom_row
    won_col = won_left_col or won_mid_col or won_right_col
    won_diag = won_left_diag or won_right_diag

    return won_row or won_col or won_diag

#print(win_check(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '], 'O'))
#print(win_check(['O', 'O', 'X', ' ', ' ', ' ', ' ', ' ', ' '], 'O'))
#print(win_check(['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' '], 'O'))
#print(win_check(['O', ' ', ' ', 'O', ' ', ' ', 'X', ' ', ' '], 'O'))
#print(win_check(['O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O'], 'O'))
#print(win_check(['O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'X'], 'O'))

import random

def choose_first_player():
    return random.randint(1, 2)

def is_position_empty(board, position):
    return board[position - 1] == ' '

def board_full_check(board):
    for elem in board:
        if elem == ' ':
            return False
    return True

def player_choice(board):
    while True:
        position = input('Choose a position (1-9): ').strip()
        if not position.isdigit():
            print("Sorry, that's not a valid position, please try again.")
            continue

        position_int = int(position)

        if not (1 <= position_int <= 9):
            print("Sorry, that's not a valid position, please try again.")
            continue

        if not is_position_empty(board, position_int):
            print("Sorry, that position has already been taken, please try again.")
            continue

        return position_int
        
# player_choice(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '])

def want_replay():
    while True:
        play_again = input('Do you want to play again? (Y/N) ').strip().upper()
        if play_again not in ['Y', 'N']:
            print("Sorry, that's not a valid choice, please try again.")
            continue
        
        return play_again == 'Y'

def play_round(board, marker, curr_player):
    display_board(board)

    print(f"It's Player {curr_player}'s turn ({marker}):")
    position = player_choice(board)

    place_marker(board, marker, position)

def get_next_player(curr_player):
    return (curr_player % 2) + 1

def play_game():
    board = [' '] * 9
    player_markers = choose_player_markers()
    curr_player = choose_first_player()
    
    while True:
        marker = player_markers[curr_player - 1]
        play_round(board, marker, curr_player)

        did_win = win_check(board, marker)
        if did_win:
            print(f'Congratulation Player {curr_player}, you win!')
            return
        
        if board_full_check(board):
            print("It's a draw")
            return
        
        curr_player = get_next_player(curr_player)
        
def play_games():
    print("Welcome to TIC TAC TOE!")    
    play = True

    while play:
        play_game()

        play = want_replay()

    print("Thank you for playing!")

play_games()