def dir_reduc(arr):
    dict = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }
    
    res = []
    n = len(arr)
    
    for i in range(n):
        if res and dict[arr[i]] == res[-1]:
            res.pop()
            continue
        res.append(arr[i])
    
    return res