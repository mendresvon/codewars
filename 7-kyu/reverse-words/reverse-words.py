def reverse_words(text):
    words = text.split(' ')
    print(words)
    result = []
    
    for word in words:
        result.append(word[::-1])
    
    return ' '.join(result)