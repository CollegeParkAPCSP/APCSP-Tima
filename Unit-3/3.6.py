# setting variables
numAdd = 100
numSub = 100
numMult = 100
numDiv = 100
numFDiv = 100
numExp = 100
numMod = 100

# change the values by 10 without using assignment operators
# use the correct operator based on the variable that is named

print("Change each value by 10 WITHOUT assignment operators:")
print("Addition: " + str(numAdd + 10) + "\nSubtraction: " + str(numSub - 10) + "\
nMultiply: "
+ str(numMult * 10) + "\nDivide: " + str(numDiv / 10) + "\nFloor Divide: " +
str(numFDiv // 10) +
"\nExponentiation: " + str(numExp ** 10) + "\nModulus: " + str(numMod % 10))

# change each value by 10 using assignment operators
# use the correct operator based on the variable that is named

numAdd += 10
numSub -= 10
numMult *= 10
numDiv /= 10
numFDiv //= 10
numExp **= 10
numMod %= 10

print("")
print("Change each value by 10 WITH assignment operators:")
print("Addition: " + str(numAdd) + "\nSubtraction: " + str(numSub) + "\nMultiply: "
+ str(numMult) + "\nDivide: " + str(numDiv) + "\nFloor Divide: " + str(numFDiv) +
"\nExponentiation: " + str(numExp) + "\nModulus: " + str(numMod))
