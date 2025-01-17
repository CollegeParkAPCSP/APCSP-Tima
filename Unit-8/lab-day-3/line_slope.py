class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.y1 = y1
        self.y2 = y2
        self.x1 = x1
        self.x2 = x2
    
    def calcSlope(self) -> str:
        return f"Slope is :: {((self.y2-self.y1) / (self.x2-self.x1)).__round__(2)}"
    
l1 = Line(1, 9, 14, 2)
l2 = Line(1, 7, 18, 3)

print(l1.calcSlope())
print(l2.calcSlope())