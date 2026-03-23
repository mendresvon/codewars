def is_valid_walk(walk):
    #determine if walk is valid
    start = [0, 0]
    if len(walk) != 10:
        return False
    
    for c in walk:
        if c == 'n':
            start[1] += 1
        elif c == 's':
            start[1] -= 1
        elif c == 'e':
            start[0] += 1
        elif c == 'w':
            start[0] -= 1
    
    if start != [0,0]:
        return False
    else:
        return True