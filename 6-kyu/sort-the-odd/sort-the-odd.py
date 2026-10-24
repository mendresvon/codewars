def sort_array(source_array):
    odds = sorted([i for i in source_array if i % 2 != 0], reverse=True)
    res = []
    
    for num in source_array:
        if num % 2 != 0:
            res.append(odds.pop())
        else:
            res.append(num)
    
    return res