import random

# recursive implementation of Bubble Sort Algorithm
def bubble_sort(array: list, max_length: int | None = None) -> None:
    if max_length is None: max_length = len(array)
    swaps = 0
    for i in range(max_length - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            swaps += 1
    if swaps > 0: bubble_sort(array, max_length - 1)

target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
bubble_sort(target_array)
print(target_array)