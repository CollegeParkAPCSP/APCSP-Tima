from Card import *
import random

class Deck:
    def __init__(self):
        suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit,name) for suit in suits for name in names]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()