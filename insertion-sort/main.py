from random import shuffle


def insertion_sort(arr: list):
    # Iterate over all elements, except the first
    for i in range(1, len(arr)):
        # Pick a key, starting from the left most side
        key = arr[i]
        # Starting from one index before that
        j = i - 1
        # Bring forth all the elements bigger than the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            # Starting going back to the starting point
            j -= 1
        # Replace the key element in its right index
        #  where all the right-side elements are bigger than it
        arr[j + 1] = key


target_array = list(range(10))
shuffle(target_array)
print(target_array)
insertion_sort(target_array)
print(target_array)
