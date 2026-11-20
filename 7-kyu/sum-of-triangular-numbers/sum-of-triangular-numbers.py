def sum_triangular_numbers(n):
    sum = 0
    to_add = 1
    
    for i in range(1, n+1):
        sum += to_add
        to_add += (i+1)
    
    return sum