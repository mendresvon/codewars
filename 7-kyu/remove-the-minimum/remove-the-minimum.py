def remove_smallest(numbers):
    n = len(numbers)
    if n < 1:
        return numbers
    
    to_remove = min(numbers)
    res = []
    for i in range(n):
        if numbers[i] == to_remove:
            res.extend(numbers[i+1:])
            break
        res.append(numbers[i])
    
    return res