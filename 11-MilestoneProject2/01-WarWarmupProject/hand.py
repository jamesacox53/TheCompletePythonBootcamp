class Hand():
    def __init__(self, player, card):
        self.player = player
        self.hand = [card]

    def add_to_player(self, player):
        player.add_cards(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def __gt__(self, other):
        our_card = self.hand[-1]
        other_card = other.hand[-1]
        
        return our_card > other_card
    
    def __eq__(self, other):
        our_card = self.hand[-1]
        other_card = other.hand[-1]
        
        return our_card == other_card