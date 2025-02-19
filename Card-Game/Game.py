from Deck import *
from Hand import *

import curses

class Game:
    def __init__(self, stdscr: curses.window):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.stdscr = stdscr

        curses.curs_set(0)

    def initial_deal(self):

        for _ in range(2):
            self.player_hand.addCard(self.deck.deal())
            self.dealer_hand.addCard(self.deck.deal())

    def player_turn(self):
        while True:
            print("\nYour hand:", self.player_hand)
            print("Hand value:", self.player_hand.getValue())
            if self.player_hand.getValue() > 21:
                print("You bust!")
                return False
            if self.player_hand.getValue() == 21:
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
            print("You busted! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busted! You win.")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("Push! It's a tie.")

    def play(self):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()

        text = "omio punched me"

        startx = int((width//2)-(len(text)//2))
        starty = int(height//2)

        # box = curses.newwin(3,30,12,50)
        # box.box()
        self.stdscr.addstr(starty, startx, text)

        self.stdscr.refresh()
        # box.refresh()

        self.initial_deal()
        print("------------- game ----------------")
        print("Dealer shows:", self.dealer_hand.cards[0])
        if not self.player_turn():
            self.determine_winner()
            return
        self.dealer_turn()
        self.determine_winner()


def main(stdscr):
    game = Game(stdscr=stdscr)
    game.play()

curses.wrapper(main)