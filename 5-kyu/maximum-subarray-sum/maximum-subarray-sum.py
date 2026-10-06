def max_sequence(arr):
    max_sum = 0
    curr_sum = 0
    
    for num in arr:
        candidate_sum = curr_sum + num
        if candidate_sum  > 0:
            curr_sum = candidate_sum
        else:
            curr_sum = 0
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum