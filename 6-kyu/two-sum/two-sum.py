def two_sum(numbers, target):
    seen = {}
    
    for idx, val in enumerate(numbers):
        dif = target-val
        if dif in seen:
            return (seen[dif], idx)
        seen[val] = idx