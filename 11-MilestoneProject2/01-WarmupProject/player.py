class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        num_cards = len(self.all_cards)

        if num_cards <= 0:
            return f'Player {self.name} has no card.'
        if num_cards == 1:
            return f'Player {self.name} has 1 card.'
        else:
            return f'Player {self.name} has {num_cards} cards.'