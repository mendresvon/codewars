def delete_nth(order,max_e):
    count = {}
    res = []
    
    for num in order:
        count[num] = 1 + count.get(num, 0)
        if count[num] > max_e:
            continue
        
        res.append(num)
    
    return res