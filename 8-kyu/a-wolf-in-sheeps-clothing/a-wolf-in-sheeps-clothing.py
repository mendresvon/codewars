def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    
    n = 0
    while queue.pop() != "wolf":
        n += 1
    
    return f"Oi! Sheep number {n}! You are about to be eaten by a wolf!"