def solve(s):
    max_sum = curr_sum = 0
    
    for char in s:
        if char in "aeiou":
            curr_sum = 0
        else:
            curr_sum += ord(char) - ord('a') + 1
        max_sum = max(curr_sum, max_sum)
    
    return max_sum