def solution(s):
    if not s:
        return ""
    words = []
    n = len(s)
    l = 0
    
    for r in range(n):
        if s[r].isupper():
            words.append(s[l:r])
            l = r
    words.append(s[l:r+1])
    return ' '.join(words)