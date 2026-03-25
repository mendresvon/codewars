from collections import deque 
def expanded_form(num):
    q = deque()
    multiplier = 1
    
    while num:
        remainder = num % 10
        if remainder != 0:
            q.appendleft(str(remainder * multiplier))
        num //= 10
        multiplier *= 10
    
    res = ' + '.join(q)
    
    return res