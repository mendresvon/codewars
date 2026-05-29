import heapq
def sum_two_smallest_numbers(numbers):
    max_heap = []
    
    for num in numbers:
        heapq.heappush(max_heap, -num)
        
        if len(max_heap) > 2:
            heapq.heappop(max_heap)
    
    return -sum(max_heap)