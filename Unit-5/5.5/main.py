def price_tag(item: str, price: float) -> str:
    n = len(item)
    if item[n-12] == item[n-1]:
        return f"{item[:-12]} is a counterfeit"
    else:
        return f"The price of {item[:-12]} is ${price}"
    
print(price_tag("socks012345543210", 5.99)) # socks is a counterfeit
print(price_tag("crackers154813564987", 1.15)) # the price of crackers is $1.15
print(price_tag("apple juice164875931246", 4.58)) # the price of apple juice is $4.58
print(price_tag("milk164812374681", 3.95)) # milk is a counterfeit
print(price_tag("xbox360s264859761278", 499.99)) # the price of xbox360s is $499.99

def alphanumeric_password(pw: str) -> int:
    n = len(pw)
    if n >= 12 and pw.isalpha():
        return 3
    elif n >= 12 and pw.isalnum():
        return 4
    elif n >= 8 and pw.isalpha():
        return 1
    elif n >= 8 and pw.isalnum():
        return 2
    return 0

print(alphanumeric_password("Pass1234")) # 2
print(alphanumeric_password("Pass!234")) # 0 (contains '!') 
print(alphanumeric_password("Short1")) # 0 (less than 8 characters) 
print(alphanumeric_password("SecurePass9")) # 2
print(alphanumeric_password("InvalidChar123")) # 4
print(alphanumeric_password("InvalidCharacters")) # 3

def remove_middle(s: str) -> str:
    n = len(s)
    if n%2 == 0:
        return s[:n//2-1] + s[n//2+1:]
    else:
        return s[:n//2] + s[n//2+1:]
    
print(remove_middle("coding")) # "cong" 
print(remove_middle("computer")) # "comter" 
print(remove_middle("hello")) # "helo" 
print(remove_middle("abcde")) # "abde" 
print(remove_middle("hello world")) # "helloworld" 
print(remove_middle("a")) # ""

def find_word_between(s: str, start: str, end: str) -> str:
    if start not in s or end not in s or s.find(start) > s.find(end):
        return ""
    return s[s.find(start)+len(start):s.find(end)]

print(find_word_between("I love Python programming!", "love", "programming")) # " Python " 
print(find_word_between("begin <data> end", "<", ">")) # "data" 
print(find_word_between("start middle end", "start", "end")) # " middle " 
print(find_word_between("no match here", "start", "end")) # "" 
print(find_word_between("oops > start", ">", "<")) # ""