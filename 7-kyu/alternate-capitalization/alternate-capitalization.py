def capitalize(s):
    a, b = list(s), list(s)
    a[::2] = s[::2].upper()
    b[1::2] = s[1::2].upper()
    return [''.join(a), ''.join(b)]