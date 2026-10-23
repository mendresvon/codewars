def two_sort(array):
    array.sort()
    return "***".join(letter for letter in array[0])