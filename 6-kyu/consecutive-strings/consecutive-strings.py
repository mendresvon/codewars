def longest_consec(strarr, k):
    n = len(strarr)
    if n==0 or k>n or k<=0:
        return ""
    
    max_len = 0
    max_str = ""
    
    for i in range(n - k + 1):
        curr_str = "".join(strarr[i:i+k]) if k > 1 else strarr[i]
        curr_len = len(curr_str)
        if curr_len > max_len:
            max_len = curr_len
            max_str = curr_str
    
    return max_str