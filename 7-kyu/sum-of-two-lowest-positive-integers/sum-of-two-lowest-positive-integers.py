import heapq
def sum_two_smallest_numbers(numbers):
    heapq.heapify(numbers)
    
    return heapq.heappop(numbers) + heapq.heappop(numbers)