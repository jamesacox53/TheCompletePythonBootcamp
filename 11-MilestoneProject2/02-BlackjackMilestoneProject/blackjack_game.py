from chips import Chips
from deck import Deck
from hand import Hand

def play_blackjack():
    print("Welcome to Blackjack")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    playing = True

    while playing:
        playing = hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break;

        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
                
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        print("\n Player's total chips are at: " + str(player_chips.total))
        new_game = input("Would you like to play another Hand? y/n ")
        if new_game.strip().lower()[0] == 'y':
            playing = True
        else:
            playing = False
            print("Thank you for playing!")

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
        
def show_some(player, dealer):
    # Show only One of dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden")
    print(dealer.cards[1])

    # Show all of player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

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

def hit(deck, hand):
    card = deck.deal()

    hand.add_card(card)
    hand.adjust_for_ace()

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
    chips.lose_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def push(player, dealer):
    print("Dealer and player tie! PUSH")


if __name__ == '__main__':
    play_blackjack()