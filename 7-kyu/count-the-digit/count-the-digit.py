def nb_dig(n, d):
    n_squares = [i**2 for i in range(n+1)]
    
    count = 0
    for square in n_squares:
        count += str(square).count(str(d))
    
    return count