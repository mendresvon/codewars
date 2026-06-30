def persistence(n):
    n = str(n)
    count = 0
    
    while len(n) > 1:
        product = 1
        for d in n:
            product *= int(d)
        n = str(product)
        count +=1 
    
    return count