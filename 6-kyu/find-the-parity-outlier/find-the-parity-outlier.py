def find_outlier(integers):
    odds = []
    evens = []
    
    for num in integers:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)
    
    return odds[0] if len(odds) < len(evens) else evens[0]