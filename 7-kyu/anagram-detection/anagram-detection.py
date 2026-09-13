# write the function is_anagram
def is_anagram(test, original):
    count_test, count_original = {}, {}
    test, original = test.lower(), original.lower()
    if len(test) != len(original):
        return False
    
    for i in range(len(original)):
        count_test[test[i]] = 1 + count_test.get(test[i], 0)
        count_original[original[i]] = 1 + count_original.get(original[i], 0)
    
    return count_test == count_original