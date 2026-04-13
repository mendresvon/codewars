def generate_hashtag(s):
    if not s:
        return False
    
    s = s.strip().title()
    words = s.split()
    
    res = "#" + "".join(words)
​
    if len(res) > 140:
        return False
    
    return res