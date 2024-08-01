from card import Card
from deck import Deck
from player import Player

def split_deck(deck, player_1, player_2):
    num_cards = len(deck.all_cards)
    
    players = (player_1, player_2)
    curr_player = 0

    for _ in range(num_cards):
        card = deck.deal_one()
        
        players[curr_player].add_cards(card)

        curr_player = (curr_player + 1) % 2    

def play_round(player_1, player_2):
    player_1_cards = []
    player_2_cards = []

    player_1_cards.append(player_1.remove_one())
    player_2_cards.append(player_2.remove_one())


def play_game(player_1, player_2):
    game_on = True
    round_num = 0

    while game_on:
        round_num += 1
        print(f'Round {round_num}:')

        if len(player_1.all_cards) == 0:
            print("player 1 is out of cards. Player 2 wins!")
            game_on = False
            break

        if len(player_2.all_cards) == 0:
            print("player 2 is out of cards. Player 1 wins!")
            game_on = False
            break
        
        play_round(player_1, player_2)

def play_war_game():
    player_1 = Player('1')
    player_2 = Player('2')

    deck = Deck()
    deck.shuffle()

    split_deck(deck, player_1, player_2)

    play_game(player_1, player_2)








if __name__ == '__main__':
    play_war_game()