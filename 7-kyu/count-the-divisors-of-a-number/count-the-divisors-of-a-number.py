def divisors(n):
    count = 1
    
    for i in range(1, int(n**1/2) + 1):
        if n % i == 0:
            count += 1
    
    return count