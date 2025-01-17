from Item import *

class VendingMachine:
    def __init__(self, admin_password="1234"):
        self.items = [Item("Chips", 2.00, 10), Item("Bar", 1.50, 10), Item("Water", 1.00, 10), Item("M&Ms", 2.00, 10)]
        self.balance = 0
        self.admin_password = admin_password

    def display_items(self):
        for i in range(len(self.items)):
            print(self.items[i].toString(i + 1))

    def insert_money(self, amount):

        if amount>0:
            self.balance += amount
            print(f"Inserted ${amount:.2f}, Current balance: ${self.balance:.2f}")
        else:
            print("That is not a valid amount")

    def select_item(self, index):
        if 1 <= index <= len(self.items):
            current_item = self.items[index]
            if not current_item.is_available():
                print(f"Sorry, {current_item.getName()} is out of stock.")
            elif self.balance < current_item.getPrice():
                print(f"Insufficient funds. {current_item.getName()} costs ${current_item.getPrice():.2f}.")
            else:
                current_item.purchase()

                self.balance -= current_item.getPrice()

                change = self.balance - current_item.getPrice()

                self.balance = 0

                print(f"Dispensing {current_item.getName()}. Change returned: ${change:.2f}")
        else:
            print("Invalid selection. Please try again.")

    def restock_items(self):
        password = input("Enter the 4-digit admin password: ")
        if password == self.admin_password:
            print("Access granted. Restocking mode activated.")
            available_indices = []
            for x in range(len(self.items)):
                # Using an f-string print out each item with the items toString method
                print(f"{self.items[x].toString(x + 1)}")

                available_indices.append(x + 1)

            restock_choice = int(input("Which item do you want to restock?"))
            if restock_choice in available_indices:
                restock_amt = int(input("How many do you want to restock?"))

                self.items[restock_choice - 1].restock(restock_amt)

                print(f"Restocked: {self.items[restock_choice - 1].getName()} with {restock_amt}")
            else:
                print("Not a valid item")
        else:
            print("Password is incorrect")

    def run(self):
        keep_running = True
        while keep_running:
            print("\n=== Vending Machine ===")
            self.display_items()
            print("\nOptions:")
            print("1: Insert money")
            print("2: Select item")
            print("3: Restock items (Admin only)")
            print("4: Quit")
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    amount = float(input("Enter the amount to insert: "))
                    self.insert_money(amount)
                case "2":
                    index = int(input("Enter the item number: "))
                    self.select_item(index)
                case "3":
                    self.restock_items()
                case "4":
                    keep_running = False

VendingMachine().run()