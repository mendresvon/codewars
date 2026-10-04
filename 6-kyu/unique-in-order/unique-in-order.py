def unique_in_order(sequence):
    res = []
    for thing in sequence:
        if not res or thing != res[-1]:
            res.append(thing)
    
    return res