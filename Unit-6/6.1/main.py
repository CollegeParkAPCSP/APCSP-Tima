def average_digits(num: str): # worse way
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

def better_av_dig(num): # better way
    s = 0
    cnt = 0
    num = int(num)
    
    while num > 0:
        s += num % 10
        num //= 10
        cnt += 1
    
    return s/cnt

x=input("Enter a number: ")
print(f'The average digit is {average_digits(x)}')

y=input("Enter a number: ")
print(f'The average digit is {better_av_dig(y)}')