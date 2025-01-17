class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0
    
    def restock(self, amount):
        if amount > 0:
            self.stock += amount
            return True
        return False
    
    def purchase(self):
        if self.is_available():
            self.stock -= 1
            return True
        
    def toString(self, index):
        # return an f-string that outputs the state of any item object in the following way
        return f'{index}: {self.name}, {self.price}, (Current stock: {self.stock})'
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getStock(self):
        return self.stock
    
    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setStock(self, stock):
        self.stock = stock