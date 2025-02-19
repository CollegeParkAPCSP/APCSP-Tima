class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
    
    def __str__(self):
        return f"{self.name} of {self.suit}"