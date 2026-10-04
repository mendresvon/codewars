def alphabet_war(fight):
    left = 0
    right = 0
    
    l_score = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
    }
    
    r_score = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1,
    }
    
    for letter in fight:
        left += l_score.get(letter, 0)
        right += r_score.get(letter, 0)
    
    if left > right:
        return "Left side wins!"
    elif left < right:
        return "Right side wins!"
    else:
        return "Let's fight again!"