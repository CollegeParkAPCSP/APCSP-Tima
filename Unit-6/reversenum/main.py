def reverse_num(num):
    result = ''
    num = int(num)
    while num > 0:
        result += str(num % 10)
        num //= 10
        
    return result

print(reverse_num(1234)) # 4321