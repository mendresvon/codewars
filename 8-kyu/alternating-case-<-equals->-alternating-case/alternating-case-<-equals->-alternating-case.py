def to_alternating_case(string):
    res = ""
    for char in string:
        if char.islower():
            res += char.upper()
        else:
            res += char.lower()
    
    return res