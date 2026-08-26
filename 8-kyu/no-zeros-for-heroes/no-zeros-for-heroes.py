def no_boring_zeros(n):
    while n % 10 == 0 and n != 0:
        n //= 10
        
    return n