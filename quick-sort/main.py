import random

# This is an ascending sorter based on Quick Sort
class AscQuickSorter:
    def __init__(self, array: list):
        self.subject = array

    def run(self, begin = 0, end = None) -> list:
        # initialize end index for first run
        if end is None: end = len(self.subject) - 1
        # make sure iteration loop is limited
        if begin < end:
            # find pivot element
            pivot = self.find_pivot(begin, end)
            # sort a partition and retrieve the partition border
            index = self.sort_partition_by_pivot(pivot, begin, end)
            # iterate the process for the higher and lower partitions
            self.run(begin, index - 1)
            self.run(index + 1, end)
        return self.subject

    # We're considering the last element as pivot
    def find_pivot(self, begin, end) -> int:
        return self.subject[begin:(end + 1)][-1]

    def sort_partition_by_pivot(self, pivot, begin, end) -> None:
        # we're on an ascending order so the first eligible position for filling is the start of partition
        next_eligible_pos = begin

        # iterate through each element of the partition
        for i in range(begin, end):
            # is the pivot greater than the element?
            if pivot >= self.subject[i]:
                # fill the eligible position with the target element
                (self.subject[next_eligible_pos], self.subject[i]) = (self.subject[i], self.subject[next_eligible_pos])
                # move the eligible position cursor one step
                next_eligible_pos += 1

        # all the lower elements have been filling the positions from starting point
        #  now we have to swap the pivot element to the next eligible positon
        (self.subject[next_eligible_pos], self.subject[end]) = (self.subject[end], self.subject[next_eligible_pos])
        # return the pivot's right (new) position
        return next_eligible_pos


target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
res = AscQuickSorter(target_array).run()
print(res)
