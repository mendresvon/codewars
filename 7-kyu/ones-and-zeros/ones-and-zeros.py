def binary_array_to_number(arr):
    mult = 2 ** (len(arr)-1)
    res = 0
    
    for bit in arr:
        res += mult * bit
        mult /= 2
​
    return res