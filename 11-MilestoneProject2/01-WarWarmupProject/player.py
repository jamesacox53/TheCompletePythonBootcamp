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

    def has_cards(self):
        return len(self.all_cards) > 0
    
    def can_go_to_war(self):
        return len(self.all_cards) >= 5

    def __str__(self):
        return self.name