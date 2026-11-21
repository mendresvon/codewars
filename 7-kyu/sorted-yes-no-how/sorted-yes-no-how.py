def is_sorted_and_how(arr):
    sorted_arr = sorted(arr)
    
    if arr == sorted_arr:
        return 'yes, ascending'
    elif arr == sorted_arr[::-1]:
        return 'yes, descending'
    else:
        return 'no'