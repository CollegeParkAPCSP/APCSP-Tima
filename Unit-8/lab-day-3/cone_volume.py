import math

class Cone:
    def __init__(self, r, h) -> None:
        self.r = r
        self.h = h
        
    def calcVolume(self) -> float:
        return ((1/3) * math.pi * self.r**2 * self.h).__round__(2)
    
cone1 = Cone(4, 4)
cone2 = Cone(4, 3)

print(cone1.calcVolume())
print(cone2.calcVolume())