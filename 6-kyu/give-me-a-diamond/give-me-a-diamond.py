def diamond(n):
    # Make some diamonds!
    if n < 0 or n%2 == 0: return None
    mid = n // 2
    res = ""
    
    for i in range(n):
        # calculate how far we are from the midpoint
        dist = abs(mid - i)
        spaces = dist
        stars = n - (dist*2)
        
        # add spaces
        res += " " * spaces
        # add stars
        res += "*" * stars
        res += "\n"
    
    return res