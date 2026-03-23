import math
​
def is_square(n):    
    if n < 0:
        return False
    
    for i in range(int(math.sqrt(n)) + 1):
        if i ** 2 == n:
            return True
    
    return False