from collections import Counter
def xo(s):
    s = s.lower()
    count = Counter(s)
    
    if 'x' not in count and 'o' not in count:
        return True
    return count['x'] == count['o']