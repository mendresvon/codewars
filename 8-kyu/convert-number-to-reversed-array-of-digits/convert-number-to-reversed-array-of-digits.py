def digitize(n):
    s = str(n)
    return [int(ch) for ch in s][::-1]