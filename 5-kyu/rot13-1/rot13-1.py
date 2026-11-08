def rot13(message):
    res = []
    for char in message:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            res.append(new_char)
        else:
            res.append(char)
    
    return ''.join(res)