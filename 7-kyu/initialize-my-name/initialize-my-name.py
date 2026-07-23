def initialize_names(name):
    name = name.split()
    res = []
    n = len(name)
    for i in range(n):
        if i == 0 or i == n-1:
            res.append(name[i])
        else:
            res.append(f"{name[i][0]}.")
    
    return ' '.join(res)