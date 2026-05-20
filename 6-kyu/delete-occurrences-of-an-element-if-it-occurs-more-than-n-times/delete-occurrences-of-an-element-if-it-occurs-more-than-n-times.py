def delete_nth(order,max_e):
    count = {}
    res = []
    
    for num in order:
        n = count.get(num, 0)
        if n >= max_e:
            continue
        
        count[num] = 1 + count.get(num, 0)
        res.append(num)
    
    return res