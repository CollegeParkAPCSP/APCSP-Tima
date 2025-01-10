class Person:
    def __init__(self, name, age, hair) -> None:
        self.name = name
        self.age = age
        self.hasHair = hair
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
    
    def setHair(self, hair):
        self.hasHair = hair
        
    def getHair(self):
        return self.hasHair
    
person1 = Person("John", 25, True)
person2 = Person("Jane", 22, False)

class Car:
    def __init__(self, make, model, mpg) -> None:
        self.make = make
        self.model = model
        self.mpg = mpg
        
    def setMake(self, make):
        self.make = make
        
    def getMake(self):
        return self.make
    
    def setModel(self, model):
        self.model = model
        
    def getModel(self):
        return self.model
    
    def setMpg(self, mpg):
        self.mpg = mpg
        
    def getMpg(self):
        return self.mpg
        
car1 = Car("Toyota", "Corolla", 30)
car2 = Car("Honda", "Civic", 35)