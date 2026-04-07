def increment_string(string):
    left = string.rstrip("0123456789")
    right = string[len(left):]
    len_right = len(right)
    
    if right == "":
        return left + '1'
    
    new_right = int(right) + 1
    
    return f"{left}{new_right:0{len_right}}"