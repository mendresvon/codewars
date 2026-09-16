def remove_url_anchor(url):
    n = len(url)
    for i in range(n):
        if url[i] == '#':
            return url[:i]
    
    return url