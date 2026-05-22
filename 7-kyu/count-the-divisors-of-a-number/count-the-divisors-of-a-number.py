def divisors(n):
    res = 1
    
    for i in range(1, int(n**1/2) + 1):
        if n % i == 0:
            res += 1
    
    return res