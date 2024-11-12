def is_vowel(c:str) -> bool:
    return c.lower() in 'aeiou'

def count_vowels(s:str) -> int:
    c = 0
    for i in s:
        if is_vowel(i):
            c += 1
    return c

def uppercase_chars(s:str) -> str:
    r = ''
    for i in s:
        if i.isupper():
            r += i
    return r

def reverse_string(s:str) -> str:
    r = ''
    for i in range(len(s)):
        r += s[-i-1]
    return r