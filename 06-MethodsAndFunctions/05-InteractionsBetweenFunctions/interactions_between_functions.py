from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)

    return my_list

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2: ')

    return int(guess)

def check_guess(shuffled_list, guess):
    if shuffled_list[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(shuffled_list)

def play_3_cup_monte():
    my_list = [' ', 'O', ' ']

    shuffled_list = shuffle_list(my_list)

    guess = player_guess()

    check_guess(shuffled_list, guess)

play_3_cup_monte()