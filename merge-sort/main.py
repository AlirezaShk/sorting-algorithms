import random, numpy as np


# This is an ascending sorter based on Merge Sort
class AscMergeSorter:
    def run(self, array) -> list:
        if len(array) > 1:
            # find the mid point
            mid = len(array)//2
            # split arrays
            left_half = array[:mid]
            right_half = array[mid:]
            # run recursively
            self.run(left_half)
            self.run(right_half)
            l = r = i = 0
            # sort and replace the data in the common length parts
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    array[i] = left_half[l]
                    l += 1
                else:
                    array[i] = right_half[r]
                    r += 1
                i += 1

            # replace the data in the remaining parts
            while l < len(left_half):
                array[i] = left_half[l]
                l += 1
                i += 1

            while r < len(right_half):
                array[i] = right_half[r]
                r += 1
                i += 1


target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
AscMergeSorter().run(target_array)
print(target_array)
