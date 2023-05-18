import random


class MaxHeapSorter():
    def __init__(self, arr: list):
        self.arr = arr

    # Evaluate the array up to the `max_len`th element, assuming current largest value resides at `largest_index`
    def heapify(self, max_len, largest_index):
        i = largest_index
        # Treat the array like a heap, evaluating left and right node values, jumping over the indices to cover the tree.
        l = 2*i + 1
        r = 2*i + 2
        if l < max_len and self.arr[l] > self.arr[i]:
            i = l
        if r < max_len and self.arr[r] > self.arr[i]:
            i = r
        # If the largest index has been changed
        if largest_index != i:
            # Set the correct largest value (at `i`) to the assumed largest value position (at `largest_index`)
            self.arr[largest_index], self.arr[i] = self.arr[i], self.arr[largest_index]
            # Repeat
            self.heapify(max_len, i)

    def sort(self):
        # Bring the max element to the root.
        for i in range(len(self.arr)//2 - 1, -1, -1):
            self.heapify(len(self.arr), i)

        for i in range(len(self.arr)-1, 0, -1):
            # Swap the root with the last element
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            # Heapify while ignoring the last element
            self.heapify(i, 0)


# import heapq
# def heapsort(arr):
#     heapq.heapify(arr)
#     n = len(arr)
#     return [heapq.heappop(arr) for i in range(n)]


target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
MaxHeapSorter(target_array).sort()
print(target_array)