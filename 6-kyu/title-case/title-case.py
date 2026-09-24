def title_case(title, minor_words=''):
    words = title.split()
    exemptions = [word.lower() for word in minor_words.split()]
    res = []
    
    for i in range(len(words)):
        if words[i].lower() not in exemptions or i == 0:
            res.append(words[i].title())
        else:
            res.append(words[i].lower())
            
    return " ".join(res)