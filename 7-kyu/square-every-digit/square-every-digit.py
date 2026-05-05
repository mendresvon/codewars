def square_digits(num):
    num = str(num)
    return int("".join([str(int(n)**2) for n in num]))