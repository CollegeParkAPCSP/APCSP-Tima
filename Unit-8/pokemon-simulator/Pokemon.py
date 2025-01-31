from Move import *
import random

class Pokemon:
    def __init__(self, name:str, type:str, health:int, move1: Move, move2: Move) -> None:
        self.name = name
        self.type = type
        self.health = health
        self.move1 = move1
        self.move2 = move2

    def attack(self, p) -> str:
        attack = random.randint(0,1)
        criticalHit = random.random()
        criticalHit = criticalHit > .9
        
        match attack:
            case 1:
                if criticalHit:
                    if p.health -self.move1.dmg*2 > 0:
                        p.setHealth(p.health-self.move1.dmg*2)
                    else: p.setHealth(0)
                    print(f"{self.name} critical hits with {self.move1.name} dealing {self.move1.dmg * 2} {self.move1.type} damage")
                else:
                    if p.health-self.move1.dmg > 0:
                        p.setHealth(p.health-self.move1.dmg)
                    else: p.setHealth(0)
                    print(f"{self.name} attacks with {self.move1.name} dealing {self.move1.dmg} {self.move1.type} damage")
            case 0:
                if criticalHit:
                    if p.health-self.move2.dmg*2 > 0:
                        p.setHealth(p.health-self.move2.dmg*2)
                    else: p.setHealth(0)
                    print(f"{self.name} critical hits with {self.move2.name} dealing {self.move2.dmg * 2} {self.move2.type} damage")
                else:
                    if p.health-self.move2.dmg > 0:
                        p.setHealth(p.health-self.move2.dmg)
                    else: p.setHealth(0)
                    print(f"{self.name} attacks with {self.move2.name} dealing {self.move2.dmg} {self.move2.type} damage")
    
    def takeDamage(self, amt:int) -> None:
        if self.health - amt < 0:
            self.health = 0
            print(f"{self.name} has fainted")
        else: 
            self.health -= amt
            print(f"{self.name} takes {amt} damage\n Remaining health: {self.health}")

    def toString(self) -> str:
        return f"Pokemon: {self.name}\nHealth: {self.health}\n----Moves----\nName: {self.move1.name}\nDamage: {self.move1.dmg}\nType: {self.move1.type}\nName: {self.move2.name}\nDamage: {self.move2.dmg}\nType: {self.move2.type}\n"
    
    def setHealth(self, newHealth:int) -> None:
        self.health = newHealth