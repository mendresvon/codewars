import heapq
​
def queue_time(customers, n):
    heap = [0] * n
    
    for c in customers:
        heapq.heapreplace(heap, heap[0] + c)
    
    return max(heap)