def nb_dig(n, d):
    squares = [str(x**2) for x in range(n+1)]
    
    count = 0
    for square in squares:
        count += square.count(str(d))
    
    return count