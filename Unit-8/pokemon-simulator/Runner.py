from Battle import *

def play():
    move1 = Move("Thunderbolt", 20, "electro")
    move2 = Move("Flamethrower", 30, "fire")
    move3 = Move("Water Gun", 40, "water")
    move4 = Move("Earthquake", 10, "ground")
    p1 = Pokemon("Pikachu", "electro", 100, move1, move2)
    p2 = Pokemon("Charizard", "fire", 100, move3, move4)
    b = Battle(p1, p2)
    b.playBattle()

play()

"""
Extensions: 
easy: health validation, critical hits, move accuracy, type effectiveness
medium: power points
totals up to 1.5 points :)
"""