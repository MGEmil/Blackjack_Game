class Card:
    def __init__(self, suit, rank):
        self.suits = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank["rank"]} of {self.suits}'

