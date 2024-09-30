# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
    
    limit = [60, 90 if not is_summer else 100]
    
    if limit[0] <= temp <= limit[1]: # python lets you do this :D
        return True
    return False

    # you could also do
    # if is_summer:
    #     return 60 <= temp <= 100
    # return 60 <= temp <= 90

print("True", squirrel_play(70, False)) # True
print("False", squirrel_play(95, False)) # False
print("True", squirrel_play(95, True)) # True
print("True", squirrel_play(90, False)) # True
print("True", squirrel_play(90, True)) # True
print("False", squirrel_play(50, False)) # False
print("False", squirrel_play(50, True)) # False
print("False", squirrel_play(100, False)) # False
print("True", squirrel_play(100, True)) # True
print("False", squirrel_play(105, True)) # False
print("False", squirrel_play(59, False)) # False
print("False", squirrel_play(59, True)) # False
print("True", squirrel_play(60, False)) # True

def sorta_sum(a: int, b: int) -> int:
    if 10 <= a + b <= 19: # if a+b in range(10, 20) also works
        return 20
    return a + b