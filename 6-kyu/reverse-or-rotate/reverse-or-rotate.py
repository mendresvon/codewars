def rev_rot(strng, sz):
    if sz > len(strng) or sz <= 0 or not strng:
        return ""
    
    start = 0
    end = sz
    res = []
    
    while end <= len(strng):
        curr_chunk = strng[start:end]
        curr_sum = sum(int(d) for d in curr_chunk)
        if curr_sum % 2 == 0:
            new_chunk = curr_chunk[::-1]
        else:
            new_chunk = curr_chunk[1:] + curr_chunk[0]
        res.append(new_chunk)
        start = end
        end += sz
            
    return "".join(res)