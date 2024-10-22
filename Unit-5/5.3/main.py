def is_same_size(str1: str, str2: str) -> bool:
    s1 = len(str1)
    s2 = len(str2)

    if s1 == s2:
        return True
    elif s1 < 4:
        return True if s1+4 == s2 else False
    return False

print(is_same_size("hello", "howdy"))
print(is_same_size("blah blah blah", "yapping"))
print(is_same_size("Happy Halloween", "Boo"))
print(is_same_size("October", "coolio"))
print(is_same_size("cow", "holycow"))

def replace_vowel(str: str) -> str:
    str = str.lower().replace('a', '1')
    str = str.lower().replace('e', '2')
    str = str.lower().replace('i', '3')
    str = str.lower().replace('o', '4')
    str = str.lower().replace('u', '5')
    return str

print(replace_vowel("The quick brown fox jumps over the lazy dog"))
print(replace_vowel("Avid diva"))
print(replace_vowel("Yo, Banana boy"))
print(replace_vowel("Never odd or even"))
print(replace_vowel("Was it a cat I saw?"))

def upper_half(str: str) -> str:
    str = str[:len(str)//2].upper() + str[-len(str)//2:].lower()
    return str

print(upper_half("HelloWorld"))
print(upper_half("Python Programming"))
print(upper_half("aBCDeFGHiJKLMNoPQRSTuVWXYZ"))
print(upper_half("ExAmPlEs"))
print(upper_half("NoNotesNoBloat"))

def find_vowel(str1: str, find: str) -> str:
    index = 0
    if find in str1:
        index = str1.find(find)
        return f"'{find}' is the {index+1}th letter in the string '{str1}'"
    else:
        return f"'{find}' is not in the string '{str1}'"
    
print(find_vowel("hello", "e"))
print(find_vowel("blahblahblah", "a"))
print(find_vowel("Halloween", "o"))
print(find_vowel("coolio", "i"))
print(find_vowel("holycow", "o"))