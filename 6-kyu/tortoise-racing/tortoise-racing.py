def race(v1, v2, gap):
    # g: gap
    # speed_dif: v2 - v1
    
    if v1 >= v2:
        return None
    
    total_hours = gap / (v2 - v1)
    total_seconds =  int(total_hours * 60 * 60) 
    
    hrs_result = total_seconds // 3600
    hrs_remainder = total_seconds % 3600
    mins_result = hrs_remainder // 60
    mins_remainder = hrs_remainder % 60
    secs_result = mins_remainder
​
    return [hrs_result, mins_result, secs_result]