"""
Extensions: 
EASY:
- type effectiveness (.25)
- move accuracy (.25)
- critical hits (.25)
- health validation (.25)

MEDIUM:
- energy or power points (.5)

TOTAL: 1.5 points :)
"""

from Battle import *

def play():
    move1 = Move("Thunderbolt", 20, "Electric", .75, 3)
    move2 = Move("Flamethrower", 30, "Fire", .75, 3)
    move3 = Move("Water Gun", 40, "Water", .75, 3)
    move4 = Move("Earthquake", 10, "Grass", .75, 3)
    p1 = Pokemon("Pikachu", "Electric", 100, move1, move2)
    p2 = Pokemon("Charizard", "Fire", 100, move3, move4)
    b = Battle(p1, p2)
    b.playBattle()

play()