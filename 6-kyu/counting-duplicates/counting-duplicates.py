def duplicate_count(text):
    unique_dict = {}
    
    for char in text:
        char = char.lower()
        unique_dict[char] = 1 + unique_dict.get(char, 0)
        
        
    return len([key for key,value in unique_dict.items() if value > 1])