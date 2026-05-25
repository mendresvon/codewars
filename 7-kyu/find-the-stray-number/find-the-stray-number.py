from collections import Counter
def stray(arr):
    count = Counter(arr)
    for key,val in count.items():
        if val == 1:
            return key