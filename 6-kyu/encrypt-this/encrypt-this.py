def encrypt_this(text):
    words = text.strip().split()
    res = []
    
    for word in words:
        first_letter = word[0]
        if len(word) < 2:
            new_string = str(ord(first_letter))
        elif len(word) == 2:
            new_string = f"{ord(first_letter)}{word[1]}"
        else:
            second_letter = word[1]
            last_letter = word[-1]
            second_letter, last_letter = last_letter, second_letter
            new_string = f"{ord(first_letter)}{second_letter}{word[2:-1]}{last_letter}"
            print(new_string)
    
        res.append(new_string)
    
    return " ".join(res)