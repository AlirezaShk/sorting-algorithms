import random
from enum import Enum


# This is a sorter based on Selection Sort Algorithm
class SelectionSorter:
    SortMode = Enum('SortMode', ['Min', 'Max'])
    def __init__(self, array: list):
        self.array = array

    def min_one_directional(self, in_place: False):
        if in_place: array = self.array
        else: array = self.array.copy()
        n = len(array)
        for i in range(n):
            min_index = i
            self.search_and_swap(array=array, start_index=i, target_index=min_index, mode=self.SortMode.Min)
        if not in_place: return array

    def max_one_directional(self, in_place: False):
        if in_place: array = self.array
        else: array = self.array.copy()
        n = len(array)
        for i in range(n):
            max_index = n - i - 1
            self.search_and_swap(array=array, start_index=i, target_index=max_index, mode=self.SortMode.Max)
        if not in_place: return array

    def search_and_swap(self, array: list, start_index: int, target_index: int, mode):
        mode = self.SortMode(mode)
        n = len(array)
        match mode:
            case self.SortMode.Min:
                for j in range(start_index, n):
                    if array[j] < array[target_index]: target_index = j
                array[start_index], array[target_index] = array[target_index], array[start_index]
                # comment: 
            case self.SortMode.Max:
                for j in range(start_index, n):
                    if array[n - j - 1] > array[target_index]: target_index = n - j - 1
                array[n - start_index - 1], array[target_index] = array[target_index], array[n - start_index - 1]
        # end match

    # The following method doesn't work.
    # def bi_directional(self, in_place: False):
    #     if in_place: array = self.array
    #     else: array = self.array.copy()
    #     n = len(array)
    #     for i in range(n):
    #         if i % 2 == 0:
    #             target_index = i
    #             mode = self.SortMode.Min
    #         else:
    #             target_index = n - i - 1
    #             mode = self.SortMode.Max
    #         self.search_and_swap(array=array, start_index=i, target_index=target_index, mode=mode)
    #     if not in_place: return array

target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
# min one directional
test1 = target_array.copy()
SelectionSorter(test1).min_one_directional(in_place=True)
print(test1)
test2 = target_array.copy()
test2_new_array = SelectionSorter(test2).min_one_directional(in_place=False)
print(test2_new_array)
# max one directional
test3 = target_array.copy()
SelectionSorter(test3).max_one_directional(in_place=True)
print(test3)
test4 = target_array.copy()
test4_new_array = SelectionSorter(test4).max_one_directional(in_place=False)
print(test4_new_array)
