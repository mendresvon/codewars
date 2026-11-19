def adjacent_element_product(array):
    max_prod = float("-inf")
    
    for i in range(len(array) - 1):
        curr_prod = array[i] * array[i+1]
        max_prod = max(curr_prod, max_prod)
    
    return max_prod