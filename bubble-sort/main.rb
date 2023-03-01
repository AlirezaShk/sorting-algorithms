def bubble_sort(array, max_length = nil)
    max_length ||= array.size
    swaps = 0
    (max_length - 1).times do |i|
        if array[i] > array[i + 1]
            array[i], array[i + 1] = array[i + 1], array[i]
            swaps += 1
        end
    end
    bubble_sort(array, max_length - 1) if swaps.positive?
end

target_array = (1..10).to_a.shuffle
puts target_array.inspect
bubble_sort target_array
puts target_array.inspect