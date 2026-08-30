def find_even_index(arr):
    l_sum = 0
    r_sum = sum(arr)
    
    for i in range(len(arr)):
        r_sum -= arr[i]
        if l_sum == r_sum:
            return i
        l_sum += arr[i]
    
    return -1