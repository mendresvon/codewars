from collections import deque
def data_reverse(data):
    n = len(data)
    d = deque()
    
    for i in range(0, n, 8):
        curr = data[i:i+8]
        d.extendleft(curr[::-1])
    
    return list(d)