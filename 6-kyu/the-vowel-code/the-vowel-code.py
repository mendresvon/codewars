def encode(st):
    d = {
        "a": "1",
        "e": "2",
        "i": "3",
        "o": "4",
        "u": "5",
    }
    res = []
    for ch in st:
        res.append(d.get(ch, ch))
    return "".join(res)
    
def decode(st):
    d = {
        "1": "a",
        "2": "e",
        "3": "i",
        "4": "o",
        "5": "u",
    }
    res = []
    for ch in st:
        res.append(d.get(ch, ch))
    return "".join(res)