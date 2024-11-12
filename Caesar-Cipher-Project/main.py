def caesar_cipher(s:str, sh:int) -> str:
    """
    Encrypts a string using a Caesar cipher.
    
    Args: 
        s (str): The decrypted string.
        sh (int): The shift. 
        
    Returns: 
        str: The encrytped text. 
    """
    
    res = ''
    for i in s:
        if i.isupper():
            pos = ord(i) - ord('A')
            pos += sh
            pos %= 26
            newchr = chr(ord('A')+pos)
            res += newchr
        elif i.islower():
            pos = ord(i) - ord('a')
            pos += sh
            pos %= 26
            newchr = chr(ord('a')+pos)
            res += newchr
        else:
            res+=i
    return res

def decrypt(s:str, sh:int) -> str:  
    """
    Decrypts a string using a Caesar cipher.
    
    Args: 
        s (str): The encrypted string.
        sh (int): The shift. 
        
    Returns: 
        str: The decrypted text. 
    """
    
    res = ''
    for i in s:
        if i.isupper():
            pos = ord(i)-ord('A')
            pos -= sh
            if pos < 0:
                pos = 26+pos
            n = chr(ord('A')+pos)
            res += n
        elif i.islower():
            pos = ord(i)-ord('a')
            pos -= sh
            if pos < 0:
                pos = 26+pos
            n = chr(ord('a')+pos)
            res += n
        else:
            res += i
    return res
            
"""
you could decrypt by converting it to ascii and subtracting 
the shift value 

symmetric encryption, because the same key is used to encrypt
and decrypt
   """