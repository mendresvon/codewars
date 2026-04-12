def sum_mul(n, m):
    if n <= 0 or m <= 0: 
        return "INVALID"
    elif n > m: 
        return 0
    
    return sum([num for num in range(n,m,n)])