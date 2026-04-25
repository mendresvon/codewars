def duplicate_encode(word):
    count = {}
    
    for char in word:
        count[char.lower()] = 1 + count.get(char.lower(), 0)
    
    res = []
    for char in word:
        if count[char.lower()] > 1:
            res.append(')')
        else:
            res.append('(')
    
    return ''.join(res)