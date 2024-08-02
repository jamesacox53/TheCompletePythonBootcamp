import random
from card import Card

class Deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    
    def __init__(self):
        deck = []

        for suit in Deck.suits:
            for rank in Deck.ranks:
                card = Card(suit, rank)

                deck.append(card)

        self.deck = deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_strs = []

        for card in self.deck:
            deck_strs.append(str(card))
        
        return '\n'.join(deck_strs)