def high(x):
    max_score = 0
    max_word = None
    words = x.split()
    
    for word in words:
        curr_score = 0
        for letter in word:
            curr_score += ord(letter) - 96
        if curr_score > max_score:
            max_score = curr_score
            max_word = word
    
    return max_word