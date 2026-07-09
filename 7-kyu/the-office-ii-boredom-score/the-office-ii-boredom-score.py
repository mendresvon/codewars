def boredom(staff):
    score = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }
    
    total = 0
    for name, dept in staff.items():
        total += score[dept]
    
    if total <= 80:
        return "kill me now"
    elif 80 < total < 100:
        return "i can handle this"
    else:
        return "party time!!"