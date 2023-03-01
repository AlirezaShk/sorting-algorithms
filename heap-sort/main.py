import heapq

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    return [heapq.heappop(arr) for i in range(n)]


target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
AscMergeSorter().run(target_array)
print(target_array)