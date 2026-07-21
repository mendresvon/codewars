def row_sum_odd_numbers(n):
    # 1: 1
    # 2: 3
    # 3: 7
    # 4: 13
    # 1 + n * (n-1)
    start = 1 + n * (n-1) # start of the row
    
    return sum(range(start, start + 2 * (n-1) + 1, 2))