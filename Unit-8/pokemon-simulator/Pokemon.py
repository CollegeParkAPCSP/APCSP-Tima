from Move import *
import random

class Pokemon:
    def __init__(self, name:str, type:str, health:int, move1: Move, move2: Move) -> None:
        self.name = name
        self.type = type
        self.health = health
        self.move1 = move1
        self.move2 = move2
        
        self.moveTypes = {
            "Fire": {"Fire":1, "Water":0.5, "Grass":2, "Electric":.5},
            "Water": {"Fire":2, "Water":1, "Grass":1, "Electric":2},
            "Grass": {"Fire":0.5, "Water":1, "Grass":1, "Electric":2},
            "Electric": {"Fire":2, "Water":0.5, "Grass":0.5, "Electric":1}
        }

    def attack(self, p):
        attack = random.randint(0,1)
        criticalHit = random.random()
        criticalHit = criticalHit > .9
        multiplier = self.moveTypes[self.type][p.type]
        health1 = p.health - (self.move1.dmg * multiplier)
        health2 = p.health - (self.move2.dmg * multiplier)
        miss1 = random.random()>self.move1.accuracy
        miss2 = random.random()>self.move2.accuracy
        
        if miss1 and attack==1 or miss2 and attack==0:
            print(f"--- {self.name} misses")
        else:
            match attack:
                case 1:
                    if self.move1.pp == 0:
                        print(f"--- {self.name} is out of {self.move1.name} PP")
                    else:
                        self.move1.pp -= 1
                        if criticalHit:
                            if health1*2 > 0:
                                p.setHealth(health1 * 2)
                            else: p.setHealth(0)
                            print(f"--- {self.name} critical hits with {self.move1.name} dealing {self.move1.dmg * 2 * multiplier} {self.move1.type} damage")
                        else:
                            if health1 > 0:
                                p.setHealth(health1)
                            else: p.setHealth(0)
                            print(f"--- {self.name} attacks with {self.move1.name} dealing {self.move1.dmg * multiplier} {self.move1.type} damage")
                            
                        print(f"\t*A multiplier of {multiplier} was applied to this attack!*")
                        
                case 0:
                    if self.move2.pp == 0:
                        print(f"--- {self.name} is out of {self.move2.name} PP")
                    else:
                        self.move2.pp -= 1
                        if criticalHit:
                            if health2*2 > 0:
                                p.setHealth(health2 * 2)
                            else: p.setHealth(0)
                            print(f"--- {self.name} critical hits with {self.move2.name} dealing {self.move2.dmg * 2 * multiplier} {self.move2.type} damage")
                        else:
                            if health2 > 0:
                                p.setHealth(health2)
                            else: p.setHealth(0)
                            print(f"--- {self.name} attacks with {self.move2.name} dealing {self.move2.dmg * multiplier} {self.move2.type} damage")
                
                        print(f"\t*A multiplier of {multiplier} was applied to this attack!*")
    
    def takeDamage(self, amt:int) -> None:
        if self.health - amt < 0:
            self.health = 0
            print(f"{self.name} has fainted")
        else: 
            self.health -= amt
            print(f"{self.name} takes {amt} damage\n Remaining health: {self.health}")

    def toString(self) -> str:
        return f"Pokemon: {self.name}\nHealth: {self.health}\n----Moves----\nName: {self.move1.name}\nDamage: {self.move1.dmg}\nType: {self.move1.type}\n\nName: {self.move2.name}\nDamage: {self.move2.dmg}\nType: {self.move2.type}\n"
    
    def setHealth(self, newHealth:int) -> None:
        self.health = newHealth