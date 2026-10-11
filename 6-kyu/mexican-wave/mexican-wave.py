def wave(people):
    res = []
    
    for i in range(len(people)):
        if people[i].isalpha():
            before = people[:i]
            curr = people[i].upper()
            after = people[i+1:] if i < len(people)-1 else ""
            res.append(before+curr+after)
    
    return res