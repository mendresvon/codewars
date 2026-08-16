def min_value(digits):
    return int(''.join([str(d) for d in sorted(set(digits))]))
    