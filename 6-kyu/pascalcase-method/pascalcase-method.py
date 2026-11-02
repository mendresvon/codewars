def camel_case(s):
    res = []
    words = s.split()
    
    for word in words:
        res.append(word[0].upper()+word[1:])
    
    return "".join(res)