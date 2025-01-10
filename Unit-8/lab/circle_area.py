import math

class Circle:
    def __init__(self, r) -> None:
        self.r = r
        
    def calcArea(self) -> float:
        return (math.pi*self.r**2).__round__(1)
    
c1 = Circle(7.5)
c2 = Circle(10)

print(c1.calcArea())
print(c2.calcArea())