from Pokemon import *
import random

class Battle:
    def __init__(self, p1:Pokemon, p2:Pokemon) -> None:
        self.p1 = p1
        self.p2 = p2

    def playRound(self) -> None:
        poke1_order = random.random()
        poke2_order = random.random()

        if poke1_order > poke2_order:
            self.p1.attack(self.p2)
            if self.p2.health>0:
                self.p2.attack(self.p1)
        print(self.toString())

    def playBattle(self) -> None:
        print(self.p1.toString())
        print(self.p2.toString())

        while self.p1.health>0 and self.p2.health>0:
            self.playRound()

        if self.p1.health>0:
            print(f"{self.p1.name} wins!")
        else:
            print(f"{self.p2.name} wins!")

    def toString(self) -> str:
        return f"{self.p1.name} has {self.p1.health} remaining health \n{self.p2.name} has {self.p2.health} remaining health"