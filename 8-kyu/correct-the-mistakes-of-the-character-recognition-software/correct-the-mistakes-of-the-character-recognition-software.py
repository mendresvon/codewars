def correct(s):
    dict = {
        '5': 'S',
        '0': 'O',
        '1': 'I',
    }
    res = ""
    for char in s:
        if char in dict:
            res += dict[char]
        else:
            res += char
    
    return res