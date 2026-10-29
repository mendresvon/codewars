def switcheroo(s):
    letter_map = {
        'a': 'b',
        'b': 'a',
    }
    
    return "".join(letter_map.get(char, char) for char in s)