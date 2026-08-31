def factorial(n):
    if 0 > n or n > 12:
        raise ValueError("Hi!")
    if n == 0:
        return 1
    return n * factorial(n-1)