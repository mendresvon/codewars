def show_sequence(n):
    if n == 0:
        return f"{n}=0"
    if n < 0:
        return f"{n}<0"
    
    sequence = "+".join([str(i) for i in range(n+1)])
    total = (n+1) * (0 + n) // 2
    
    return f"{sequence} = {total}"