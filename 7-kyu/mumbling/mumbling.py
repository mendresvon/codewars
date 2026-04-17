def accum(st):
    return "-".join(s.upper() + s.lower() * i for i,s in enumerate(st))