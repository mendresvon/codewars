def sort_array(source_array):
    odds = sorted([i for i in source_array if i % 2 != 0], reverse=True)
    res = [num if num % 2 == 0 else odds.pop() for num in source_array]
    return res