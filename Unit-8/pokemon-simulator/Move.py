class Move:
    def __init__(self, name:str, dmg:int, type:str) -> None:
        self.name = name
        self.dmg = dmg
        self.type = type

    def getDmg(self):
        return self.dmg
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def setDmg(self, newDmg):
        self.dmg = newDmg

    def setName(self, newName):
        self.name = newName

    def setType(self, newType):
        self.type = newType

    def toString(self):
        return f"Name: {self.name}, \nDamage Amount: {self.dmg}, \nType: {self.type}"