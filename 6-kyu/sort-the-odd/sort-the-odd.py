import heapq
def sort_array(source_array):
    odds = [i for i in source_array if i % 2 != 0]
    heapq.heapify(odds)
    res = [num if num % 2 == 0 else heapq.heappop(odds) for num in source_array]
    return res