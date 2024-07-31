import random
from card import Card

class Deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    
    def __init__(self):
        all_cards = []

        for suit in Deck.suits:
            for rank in Deck.ranks:
                card = Card(suit, rank)

                all_cards.append(card)

        self.all_cards = all_cards

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    