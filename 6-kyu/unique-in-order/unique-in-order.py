def unique_in_order(sequence):
    res = []
    for thing in sequence:
        if len(res) == 0 or thing != res[-1]:
            res.append(thing)
    
    return res