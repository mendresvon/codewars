def expanded_form(num):
    q = []
    multiplier = 1
    
    while num:
        remainder = num % 10
        if remainder != 0:
            q.append(str(remainder * multiplier))
        num //= 10
        multiplier *= 10
    
    res = f"{q.pop()}"
    
    while q:
        res += f" + {q.pop()}"
    
    return res