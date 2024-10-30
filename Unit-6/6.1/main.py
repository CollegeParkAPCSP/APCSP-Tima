def average_digits(num: str):
    index = 0
    sum = 0
    n = len(num)
    
    if num.isdigit():
        while index < n:
            digit = int(num[index])
            sum += digit
            index += 1
    else: 
        return "Invalid input"
    return sum/n

print(average_digits("1234")) # 2.5