def user_choice():
    choice = 'Wrong'
    
    while not choice.isdigit():
        choice = input('Please enter a number (0-10): ')

        if not choice.isdigit():
            print("Sorry, that is not a digit.")

    return int(choice)

# user_choice()

def user_choice2():
    choice = 'Wrong'
    choice_int = 0
    acceptable_range = range(0, 10)
    within_range = False

    while not choice.isdigit() or not within_range:
        choice = input('Please enter a number (0-10): ')

        if choice.isdigit():
            choice_int = int(choice)
            if choice_int in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of the acceptable range (0-10).")
        else:
            print("Sorry, that is not a digit.")

    return choice_int

user_choice2()