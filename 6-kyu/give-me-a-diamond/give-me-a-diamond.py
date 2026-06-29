def diamond(n):
    if n < 0 or n%2 == 0:
        return None
    
    mid = n // 2
    res = ""
    for i in range(n):
        # calc how far current iteration is from mid
        dist = abs(mid - i)
        spaces = dist
        stars  = n - (2*dist)
        
        for j in range(spaces):
            res += " "
        for k in range(stars):
            res += "*" 
        res += "\n"
    
    return res