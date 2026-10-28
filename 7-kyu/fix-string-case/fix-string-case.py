def solve(s):
    low_count = 0
    up_count = 0
    for letter in s:
        if letter.islower():
            low_count += 1
        else:
            up_count += 1
    
    if low_count >= up_count:
        return s.lower()
    else:
        return s.upper()