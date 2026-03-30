def disemvowel(string_):
    vowels = set("aeiouAEIOU")
    res = [c for c in string_ if c not in vowels]
    return ''.join(res)