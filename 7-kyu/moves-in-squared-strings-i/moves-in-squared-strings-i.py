def vert_mirror(strng):
    return '\n'.join(word[::-1] for word in strng.split('\n'))
    
def hor_mirror(strng):
    return '\n'.join([word for word in strng.split('\n')][::-1])
    
def oper(fct, s):
    return fct(s)