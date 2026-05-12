def count(s):
    count = {}
    
    for char in s:
        count[char] = 1 + count.get(char, 0)
    
    return count