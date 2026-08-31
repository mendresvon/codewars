def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
    if n == 0:
        return 1
    return n * factorial(n-1)