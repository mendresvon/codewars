def accum(st):
    res = []
    
    count = 1
    for c in st:
        curr = (c*count).title()
        res.append(curr)
        count += 1
    
    return '-'.join(res)