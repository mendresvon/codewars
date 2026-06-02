def is_pangram(st):
    st = set([s.lower() for s in st if s.isalpha()])
    
    return len(st) == 26