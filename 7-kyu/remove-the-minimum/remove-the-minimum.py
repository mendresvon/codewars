def remove_smallest(numbers):
    if not numbers: return []
    low = min(numbers)
    
    res = []
    for i in range(len(numbers)):
        if numbers[i] == low:
            res.extend(numbers[i+1:])
            break
        res.append(numbers[i])
    
    return res