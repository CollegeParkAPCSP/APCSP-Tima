def reverse_num(num):
    result = ''
    num = int(num)
    while num > 0:
        result += str(num % 10)
        num //= 10
    return result

def sum_of_digits(num):
    res = 0
    num = int(num)
    while num > 0:
        res += num % 10
        num //= 10
    return res

def multiple_of_threes(n):
    return 'x'*(n//3)