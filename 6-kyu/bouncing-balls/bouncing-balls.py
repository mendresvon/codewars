def bouncing_ball(h, bounce, window):
    # your code
    if not(h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    res = 0
    while h > window:
        res += 1
        h *= bounce
        if h > window:
            res += 1
    
    return res