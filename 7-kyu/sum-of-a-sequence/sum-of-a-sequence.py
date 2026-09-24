def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    summ = 0
    
    while begin_number <= end_number:
        summ += begin_number
        begin_number += step
    
    return summ