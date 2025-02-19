from Card import *

class Player:
    def __init__(self):
        self.cards = []
        self.total = 0

    def checkAce(self):
        if self.total + 11 > 21:
            self.cards[self.cards.index()]

    def addCard(self, card: Card):
        self.cards.append(card)
        self.total += card.getVal()