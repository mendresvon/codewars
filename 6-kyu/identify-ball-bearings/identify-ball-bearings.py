def identify_bb(bearings, weigh):
    to_weigh = []
    count = 0
    for idx, bearing in enumerate(bearings):
        to_weigh.extend([bearing] * idx)
        
    expected_weight = 10 * len(to_weigh)
    actual_weight = weigh(*to_weigh)
    difference = actual_weight - expected_weight
    
    return bearings[difference]