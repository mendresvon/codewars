def increment_string(string):
    left = string.rstrip("0123456789")
    right = string[len(left):]
    if right == "":
        return left + '1'
    return f"{left}{int(right) + 1:0{len(right)}}"