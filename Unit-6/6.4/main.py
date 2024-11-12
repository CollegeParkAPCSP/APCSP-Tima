def make_six(word: str) -> str:
    if len(word) >=6:
        return word
    else:
        res = ''
        while len(res) < 6:
            res += word
    return res

def count_even_and_odd(num) -> str:
    n = str(num)
    even=0
    odd=0
    for i in range(len(n)):
        if int(n[i])%2==0:
            even+=1
        else:
            odd+=1
    return f'Even: {even}\n Odd: {odd}'