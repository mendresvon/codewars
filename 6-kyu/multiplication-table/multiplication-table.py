def multiplication_table(size):
    res = []
    
    for i in range(1, size+1):
        curr = []
        for j in range(1, size+1):
            curr.append(i*j)
        res.append(curr)
    
    return res