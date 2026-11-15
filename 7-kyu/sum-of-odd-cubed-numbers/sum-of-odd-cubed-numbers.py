def cube_odd(arr):
    total = 0
    
    for x in arr:
        if type(x) is not int:
            return None
        if x % 2 == 1:
            total += x**3
    
    return total