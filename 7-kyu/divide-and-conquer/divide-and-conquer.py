def div_con(x):
    total = 0
    for element in x:
        if type(element) is int:
            total += element
        else:
            total -= int(element)
    
    return total