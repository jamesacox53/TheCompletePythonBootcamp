class Hand():
    values = { 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11 }
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        
        value = self.values[card.rank]
        self.value += value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # Change Ace to be a 1 instead of 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1