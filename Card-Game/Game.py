import random

class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
    
    def __str__(self):
        return f"{self.name} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit,name) for suit in suits for name in names]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
    
    def getValue(self):
        total = 0
        aces = 0

        for card in self.cards:
            if card.name in ["J", "Q", "K"]:
                total += 10
            elif card.name == "A":
                total += 11
                aces += 1
            else:
                total += int(card.name)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        for i in range(2):
            self.player_hand.addCard(self.deck.deal())
            self.dealer_hand.addCard(self.deck.deal())

    def player_turn(self):
        while True:
            print("\nYour hand:", self.player_hand)
            print("Hand value:", self.player_hand.getValue())
            if self.player_hand.getValue() > 21:
                print("You bust!")
                return False
            if self.dealer_hand.getValue() == 21 and len(self.dealer_hand.cards) == 2:
                print("Dealer has blackjack!")
                return False
            if self.player_hand.getValue() == 21 and len(self.player_hand.cards) == 2:
                print("Blackjack!")
                return False
            choice = input("Do you want to 'hit' or 'stand'? ").lower().strip()
            if choice == "hit":
                card = self.deck.deal()
                if card is None:
                    print("No more cards in the deck!")
                    break
                self.player_hand.addCard(card)
            elif choice == "stand":
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")
        return True

    def dealer_turn(self):
        print("\nDealer's turn:")
        print("Dealer's hand:", self.dealer_hand)
        while self.dealer_hand.getValue() < 17:
            print("Dealer hits.")
            card = self.deck.deal()
            if card is None:
                break
            self.dealer_hand.addCard(card)
            print("Dealer's hand now:", self.dealer_hand)
        print("Dealer stands with a value of:", self.dealer_hand.getValue())

    def determine_winner(self):
        player_value = self.player_hand.getValue()
        dealer_value = self.dealer_hand.getValue()
        print("\nFinal hands:")
        print("Your hand:", self.player_hand, f"(Value: {player_value})")
        print("Dealer's hand:", self.dealer_hand, f"(Value: {dealer_value})")

        if player_value > 21:
            print("\u001b[1;31mYou busted! Dealer wins.\u001b[0;37m")
        elif dealer_value > 21:
            print("\u001b[1;32mDealer busted! You win.\u001b[0;37m")
        elif player_value > dealer_value:
            print("\u001b[1;32mYou win!\u001b[0;37m")
        elif player_value < dealer_value:
            print("\u001b[1;31mDealer wins.\u001b[0;37m")
        else:
            print("\u001b[1;37mPush! It's a tie.\u001b[0;37m")

    def play(self):
        self.initial_deal()
        print("------------- game ----------------")
        print("Dealer shows:", self.dealer_hand.cards[0])
        if not self.player_turn():
            self.determine_winner()
            return
        self.dealer_turn()
        self.determine_winner()

if __name__ == "__main__":
    game = Game()
    game.play()