def find_missing_letter(chars):
    n = len(chars)
    
    for i in range(n-1):
        if ord(chars[i+1]) - ord(chars[i]) != 1:
            return chr(ord(chars[i]) + 1)
    
​
        