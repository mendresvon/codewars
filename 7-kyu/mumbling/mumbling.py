def accum(st):
    return "-".join((c * i).capitalize() for i, c in enumerate(st, 1))