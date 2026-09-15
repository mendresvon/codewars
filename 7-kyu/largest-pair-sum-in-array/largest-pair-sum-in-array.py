def largest_pair_sum(numbers): 
    max1 = float('-inf')
    max2 = float('-inf')
    
    for i in numbers:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    
    return max1 + max2