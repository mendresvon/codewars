def in_array(array1, array2):
    res = set()
    
    for s1 in array1:
        for s2 in array2:
            if s1 in s2:
                res.add(s1)
                break
    
    return sorted(list(res))