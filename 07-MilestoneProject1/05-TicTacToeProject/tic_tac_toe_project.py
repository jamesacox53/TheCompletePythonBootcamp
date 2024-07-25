def display_board(board):
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print(f'---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(f'---+---+---')
    print(f' {board[0]} | {board[1]} | {board[2]} ')

display_board([' ', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'])

def player_input():
    p1_choice = ''

    while p1_choice not in ['X', 'O']:
        p1_choice = input('Player 1 do you want to be X or O? ')

        if p1_choice not in ['X', 'O']:
            print("Sorry, you can't be that.")

    if p1_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
print(player_input())