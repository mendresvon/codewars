def move_zeros(lst):
    if not lst: return []
    non_zeroes = []
    zeroes = []
​
    for num in lst:
        if num == 0:
            zeroes.append(num)
        else:
            non_zeroes.append(num)
    
    non_zeroes.extend(zeroes)
    return non_zeroes