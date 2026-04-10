def hungry_seven(digits: list[int]) -> list[int]:
    copy = digits[:]
    n = len(digits)
    
    while True:
        changed = False
        for i in range(n-2):
            if copy[i:i+3] == [7,8,9]:
                copy[i], copy[i+1], copy[i+2] = 8, 9, 7
                changed = True
            
        if not changed:
            break
        
    return copy