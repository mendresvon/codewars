def persistence(n):
    digits = [int(d) for d in str(n)]
    count = 0
    
    while len(digits) > 1:
        product = 1
        for d in digits:
            product *= d
        digits = [int(d) for d in str(product)]
        count +=1 
    
    return count