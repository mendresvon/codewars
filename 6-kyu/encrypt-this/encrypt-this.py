def encrypt_this(text):
    words = text.strip().split()
    
    res = []
    for word in words:
        first = str(ord(word[0]))
        if len(word) == 1:
            res.append(first)
        elif len(word) == 2:
            res.append(first + word[1])
        else:
            res.append(f"{first}{word[-1]}{word[2:-1]}{word[1]}")
    
    return " ".join(res)