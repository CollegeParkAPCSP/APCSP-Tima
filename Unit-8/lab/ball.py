class Ball:
    def __init__(self, ap:int, apc:int, color:str, type:str) -> None:
        self.color = color
        self.type = type
        self.ap = ap
        self.apc = apc
        
    def getColor(self) -> str:
        return self.color
    
    def getType(self) -> str:
        return self.type
    
    def getPressure(self) -> int:
        return self.ap
    
    def getCapacity(self) -> int:
        return self.apc
    
    def isFull(self) -> bool:
        return self.ap >= self.apc/2
    
    def isFlat(self) -> bool:
        return self.ap < self.apc/2
    
    def needsAir(self) -> int:
        return self.apc - self.ap
    
    def addAir(self, n) -> bool:
        if self.ap < self.apc:
            self.ap += n
            return True
        else:
            return False
        
        
b = Ball( 11, 30, "RED", "BASKETBALL" )
print( "AIR Pressure " + str(b.getPressure()) )
print( "AIR Capacity " + str(b.getCapacity() ))
print( "BALL Color " + b.getColor() )
print( "BALL Type " + b.getType() )
print( "Is Ball full of AIR " + str(b.isFull() ))
print( "How much air is needed " + str(b.needsAir() ))
print( "Is Ball FLAT " + str(b.isFlat() ))
print( "Adding 20 to pressure " + str(b.addAir(20) ))
print( "Adding 20 to pressure " + str(b.addAir(20) ))
print( "Is Ball full of AIR " + str(b.isFull() ))
print( "Is Ball FLAT " + str(b.isFlat() ))