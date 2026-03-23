def find_outlier(integers):
    odd_count = 0
    even_count = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    outlier_remainder = 0
    if even_count > odd_count:
        outlier_remainder = 1
    else:
        outlier_remainder = 0
        
    for num in integers:
        if num % 2 == outlier_remainder:
            return num