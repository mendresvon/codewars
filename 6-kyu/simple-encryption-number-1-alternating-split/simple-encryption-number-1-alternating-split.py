def decrypt(text, n):
    for _ in range(n):
        mid = len(text) // 2
        odd_idx = text[:mid]
        even_idx = text[mid:]
        min_len = min(len(odd_idx), len(even_idx))
        res = "".join([even_idx[i] + odd_idx[i] for i in range(min_len)])
        text = res + odd_idx[min_len:] + even_idx[min_len:]
    return text
​
def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    
    return text