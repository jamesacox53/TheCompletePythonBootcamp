from deck import Deck
from player import Player
from hand import Hand

def play_war_game():
    player_1 = get_player(1)
    player_2 = get_player(2)
    players = (player_1, player_2)

    add_player_cards(players)

    play_game(players)

def get_player(player_num):
    player_name = input(f'Player {player_num} please input\' your name: ')

    return Player(player_name)

def add_player_cards(players):
    deck = Deck()
    deck.shuffle()

    num_players = len(players)
    deck_partitions = deck.split_deck(num_players)

    for i in range(num_players):
        player = players[i]
        partition = deck_partitions[i]

        player.add_cards(partition)

def play_game(players):
    round_num = 0

    while True:
        if check_if_game_over(players):
            return True
        
        round_num += 1
        print(f'Round {round_num}:')

        play_round(players)

def check_if_game_over(players):
    players_still_playing = []

    for player in players:
        if player.has_cards():
            players_still_playing.append(player)

    if len(players_still_playing) == 0:
        print('No players are able to play so game ends in a Draw!')
        return True
    elif len(players_still_playing) == 1:
        print(f'Player {players_still_playing[0]} has Won!')
        return True
    else:
        return False

def play_round(players):
    players_hands = []

    for player in players:
        card = player.remove_one()
        
        player_hand = Hand(player, card)
        players_hands.append(player_hand)

    play_hands(players_hands)

def play_hands(players_hands):
    best_hands = get_best_hands(players_hands)

    if len(best_hands) == 1:    
        won_the_round(best_hands[0], players_hands) 
    else:
        print('WAR!')
        go_to_war(best_hands)

def get_best_hands(players_hands):
    best_hands = [players_hands[0]]

    for i in range(1, len(players_hands)):
        player_hand = players_hands[i]
        best_hand = best_hands[0]

        if player_hand > best_hand:
            best_hands = [player_hand]
        
        elif player_hand == best_hand:
            best_hands.append(player_hand)

    return best_hands

def won_the_round(winning_player_hand, players_hands):
    player = winning_player_hand.player
    print(f'Player {player} has won the round!')
    
    add_cards(player, players_hands)

def add_cards(player, players_hands):
    for player_hand in players_hands:
        player_hand.add_to_player(player)

def go_to_war(players_hands):
    war_hands = get_war_hands(players_hands)

    if len(war_hands) == 0:
        won_the_war(players_hands[0], players_hands)
    elif len(war_hands) == 1:
        won_the_war(war_hands[0], players_hands)
    else:
        commence_war(war_hands)

def get_war_hands(players_hands):
    war_hands = []

    for player_hand in players_hands:
        player = player_hand.player

        if player.can_go_to_war():
            for _ in range(5):
               card = player.remove_one()
               player_hand.add_card(card)

            war_hands.append(player_hand)

    return war_hands

def won_the_war(winning_player_hand, players_hands):
    player = winning_player_hand.player
    print(f'Player {player} has won the war!')

    add_cards(player, players_hands)

def commence_war(war_hands):
    best_hands = get_best_hands(war_hands)

    if len(best_hands) == 1:    
        won_the_war(best_hands[0], war_hands) 
    else:
        go_to_war(best_hands)


if __name__ == '__main__':
    play_war_game()