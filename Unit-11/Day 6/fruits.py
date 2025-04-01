file = open("fruits.dat", "r")
fruits_data = [line for line in file]
validFruits = 'applebananaorange'
valid_fruits = []

for i in fruits_data:
    if i.lower().strip() in validFruits:
        print(i.lower().strip())
        valid_fruits.append(i.lower().strip())

valid_apples = valid_fruits.count('apple')
valid_bananas = valid_fruits.count('banana')
valid_oranges = valid_fruits.count('orange')

print(f"Valid Apples: {valid_apples}")
print(f"Valid Bananas: {valid_bananas}")
print(f"Valid Oranges: {valid_oranges}")
