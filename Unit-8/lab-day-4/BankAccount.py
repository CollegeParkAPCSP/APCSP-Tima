class BankAccount:
    def __init__(self, owner, limit, balance=0) -> None:
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def deposit(self, amount) -> str:
        if amount > 0 and amount + self.balance <= self.limit:
            self.balance += amount
            return f"New balance: {self.balance}"
        elif amount + self.balance > self.limit:
            return "Deposit exceeds limit"
        else: return "Invalid amount"
    
    def withdraw(self, amount) -> str:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"New balance: {self.balance}"
        else: return "Invalid amount"
        
    def check_balance(self) -> str:
        return f"Current balance: {self.balance}"