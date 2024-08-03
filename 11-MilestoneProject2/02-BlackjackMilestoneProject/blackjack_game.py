from chips import Chips

def take_bet(chips):
    while True:
        try:
            bet_amount = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer.")
            continue

        if bet_amount > chips.total:
            print(f"Sorry, you don't have enough chips. You have {chips.total} chips.")
            continue

        chips.bet = bet_amount
        break
        
def hit(deck, hand):
    card = deck.deal()

    hand.add_card(card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    while True:
        choice = input("Hit or Stand? Please enter h or s: ")
        choice = choice.lower().strip()
        first_letter = choice[0]

        if first_letter == 'h':
            hit(deck, hand)
        
        elif first_letter == 's':
            print("Player stands. Dealer's turn.")
            return False

        else:
            print("Sorry I didn't understand that, please enter h or s only.")

def show_some(player, dealer):
    # Show only One of dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden")
    print(dealer.cards[1])

    # Show all of player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # Show all of dealer's cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    
    print("Value of Dealer's hand: " + str(dealer.value))
    
    # Show all of player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

    print("Value of Player's hand: " + str(player.value))

def player_busts(player, dealer, chips):
    print("PLAYER BUST!")
    chips.lost_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lost_bet()

def push(player, dealer):
    print("Dealer and player tie! PUSH")