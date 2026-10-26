def high(x):
    max_score = 0
    max_word = ""
    words = x.split()
    
    for word in words:
        curr_score = 0
        for letter in word:
            curr_score += ord(letter) - ord('a') + 1
        if curr_score > max_score:
            max_score = curr_score
            max_word = word
    
    return max_word