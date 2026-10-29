def switcheroo(s):
    table = str.maketrans("ab", "ba")
    return s.translate(table)