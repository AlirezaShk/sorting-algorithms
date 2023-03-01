# This is an ascending sorter based on Merge Sort
class AscMergeSorter
    def self.run array
        n = array.size
        return unless n > 1

        # find the mid point
        mid = n / 2
        # split arrays
        left_half = array[0..(mid - 1)]
        right_half = array[mid..n]
        # run recursively
        run(left_half)
        run(right_half)
        i = r = l = 0
        # loop through all elements until everything is covered for
        until  r >= right_half.size and l >= left_half.size
            # if left_element is nil => Choose right element
            # if left_element is not nil, right_element is nil => Choose left element
            # if left_element is not nil, right_element is not nil => Compare values
            if left_half[l].nil? || (!right_half[r].nil? && right_half[r] < left_half[l])
                array[i] = right_half[r]
                r += 1
            else
                array[i] = left_half[l]
                l += 1
            end
            i += 1
        end
    end
end

target_array = (1..10).to_a.shuffle
puts target_array.inspect
res = AscMergeSorter.run(target_array)
puts target_array.inspect
