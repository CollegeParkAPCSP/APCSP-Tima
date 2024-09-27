import math
import random as r

x = float(input("Enter a float (x): "))
y = int(input("Enter an integer (y): "))

sqrtx = math.sqrt(x)
sqrty = math.sqrt(y)
absx = math.fabs(x)
expx = math.exp(x)
expy = math.exp(y)
ceil = math.ceil(x)
floor = math.floor(x)
logx = math.log(x, 10)
logy = math.log(y, 10)
powxy = math.pow(x, y)
powyx = math.pow(y, x)
randint = r.randint(int(x), y)
rr = r.randrange(int(x), y)
r1 = r.random() * x * y
r2 = r.random() * x * y

print("sqrt(x) = ", sqrtx)
print("sqrt(y) = ", sqrty)
print("abs(x) = ", absx)
print("e ^ x = ", expx)
print("e ^ y = ", expy)
print("ceil(x) = ", ceil)
print("floor(x) = ", floor)
print("logbase 10 (x) = ", logx)
print("logbase 10 (y) = ", logy)
print("x ^ y = ", powxy)
print("y ^ x = ", powyx)
print("randint = ", randint)
print("randrange = ", rr)
print("random * both nums = ", r1)
print("another random * both nums = ", r2)
