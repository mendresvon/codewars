def solution(s):
    res = []
    
    for i in range(0, len(s), 2):
        curr_char = s[i]
        next_char = s[i+1] if i+1 < len(s) else '_'
        res.append(f"{curr_char}{next_char}")
    
    return res