from collections import Counter
def find_uniq(arr):
    count = Counter(arr)
    
    for num, c in count.items():
        if c == 1:
            return num