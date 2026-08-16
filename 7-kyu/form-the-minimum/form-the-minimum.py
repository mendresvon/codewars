def min_value(digits):
    digits = set(digits)
    digits = sorted(list(digits))
    res = [str(d) for d in digits]
    return int(''.join(res))