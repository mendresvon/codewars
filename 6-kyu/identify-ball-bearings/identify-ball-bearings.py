def identify_bb(bearings, weigh):
    to_weigh = []
    
    for idx, bearing in enumerate(bearings):
        to_weigh.extend([bearing] * idx)
    
    actual_weight = weigh(*to_weigh)
    expected_weight = len(to_weigh) * 10
    
    return bearings[actual_weight - expected_weight]