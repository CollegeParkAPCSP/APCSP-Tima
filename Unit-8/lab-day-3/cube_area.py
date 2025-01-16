class Cube:
    def __init__(self, s) -> None:
        self.s = s
        
    def calcArea(self) -> str:
        return f"Cube area is :: {(float(6*self.s**2)).__round__(1)}"
    
cube1 = Cube(112)
cube2 = Cube(4)

print(cube1.calcArea())
print(cube2.calcArea())