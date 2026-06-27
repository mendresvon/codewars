def capitals(word):
    if not word: return
    res = [i for i,c in enumerate(word) if c.isupper()]
    return res