def series_sum(n):
    if not n: return '0.00'
    
    denominator = 4
    res = 1
    
    for i in range(1, n):
        rate = 1/denominator
        res += (rate)
        denominator += 3
    
    return f"{res:.2f}"