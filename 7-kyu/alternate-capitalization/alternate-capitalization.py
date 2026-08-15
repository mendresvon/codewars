def capitalize(s):
    res = [[], []]
    for i, c in enumerate(s):
        if i % 2 == 0:
            res[0].append(c.upper())
            res[1].append(c)
        else:
            res[0].append(c)
            res[1].append(c.upper())
    
    return [''.join(res[0]), ''.join(res[1])]