def series_sum(n):
    res = 0
    
    for i in range(n):
        res += 1 / (1 + 3 * float(i))
    
    return f"{res:.2f}"