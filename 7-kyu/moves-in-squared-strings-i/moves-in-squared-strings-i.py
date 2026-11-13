def vert_mirror(strng):
    words = strng.split("\n")
    res = []
    for word in words:
        res.append(word[::-1])
    return "\n".join(res)
    
def hor_mirror(strng):
    words = strng.split("\n")
    front = 0
    back = len(words) - 1
    
    while front < back:
        words[front], words[back] = words[back], words[front]
        front += 1
        back -= 1
    
    return "\n".join(words)
    
def oper(fct, s):
    return fct(s)