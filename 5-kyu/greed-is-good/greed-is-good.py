def score(dice):
    count = {} # store the count of each roll    
    for roll in dice:
        count[roll] = 1 + count.get(roll, 0)
    
    # for the threes of one number
    values = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200,
    }
    res = 0
    for key, val in count.items():
        while val > 0:
            if val >= 3:
                val -= 3
                res += values[key]
                continue
            
            if key == 1:
                res += 100
            elif key == 5:
                res += 50
            val -= 1
    
    return res