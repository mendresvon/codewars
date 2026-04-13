def pofi(n):
    d = {
        0: '1',
        1: 'i',
        2: '-1',
        3: '-i',
    }
    
    return d[n%4]