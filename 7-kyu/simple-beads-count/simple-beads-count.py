def count_red_beads(n):
    res = 0
    n -= 1
    while n > 0:
        res += 2
        n -= 1
    
    return res