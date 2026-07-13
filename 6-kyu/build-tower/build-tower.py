def tower_builder(n_floors):
    res = []
    
    for i in range(n_floors):
        spaces = ' ' * (n_floors - i - 1)
        stars = '*' * (1 + i * 2)
        res.append(spaces + stars + spaces)
    
    return res