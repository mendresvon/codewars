from collections import Counter
def find_it(seq):
    if len(seq) == 1:
        return seq[0]
    
    count = Counter(seq)
    
    return [val for val,count in count.items() if count % 2 != 0][0]