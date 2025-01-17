from BankAccount import BankAccount

# Create a new account
account = BankAccount("Alice", 500, 100)

# Test deposit
print(account.deposit(50)) # Should increase balance to 150

# Test withdrawal
print(account.withdraw(30)) # Should decrease balance to 120

# Test invalid withdrawal
print(account.deposit(1000)) # Should return an error