def multiple_of_index(arr):
    return [
        val for idx, val in enumerate(arr)
        if (idx == 0 and val == 0) or (idx != 0 and val % idx == 0)
    ]