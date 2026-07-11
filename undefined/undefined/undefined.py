def freq_detect(freq):
    res = []
    prev = 0
    
    for num in freq:
        dif = num - prev
        if dif == 0:
            res.append('-')
        elif dif >= 0:
            res.append('/' * dif)
        else: # if dif is negative
            res.append('_' * -dif)
        prev = num
    
    return res