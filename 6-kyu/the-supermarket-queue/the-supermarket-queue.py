import heapq
def queue_time(customers, n):
    heap = [0] * n
    
    for c in customers:
        heapq.heappushpop(heap, heap[0]+c)
        
    return max(heap)