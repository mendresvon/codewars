def rot13(message):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    res = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_idx = (ord(char.lower()) - ord('a') + 13) % 26
                new_char = alphabet[new_idx].upper()
                res.append(new_char)
            else:
                new_idx = (ord(char.lower()) - ord('a') + 13) % 26
                new_char = alphabet[new_idx]
                res.append(new_char)
        else:
            res.append(char)
    
    return ''.join(res)