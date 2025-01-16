class Trapeziod:
    def __init__(self, base1, base2, height) -> None:
        self.base1 = base1
        self.base2 = base2
        self.height = height
        
    def calcArea(self) -> float:
        return (0.5 * (self.base1 + self.base2) * self.height).__round__(1)
    
trap1 = Trapeziod(3, 3, 3)
trap2 = Trapeziod(5, 6, 7)

print(trap1.calcArea())
print(trap2.calcArea())