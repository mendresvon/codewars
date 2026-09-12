def sum_of_minimums(numbers):
    total = 0
    for row in numbers:
        total += min(row)
    return total