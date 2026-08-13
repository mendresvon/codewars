def binary_array_to_number(arr):
    multiplier = 2 ** (len(arr) - 1)
    print(multiplier)
    res = 0
    
    for bit in arr:
        res += (multiplier * bit)
        multiplier //= 2
    
    return res