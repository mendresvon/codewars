from collections import Counter
def find_uniq(arr):
    count = Counter(arr)
    
    for idx,val in count.items():
        if val == 1:
            return idx