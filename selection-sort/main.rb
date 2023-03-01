# This is a sorter based on Selection Sort Algorithm
class SelectionSorter
    SORT_MODE = %i(min max)
    def initialize(array)
        @array = array
    end

    def min_one_directional(in_place: false)
        array = in_place ? @array : @array.clone
        array.size.times do |i|
            min_index = i
            search_and_swap(array, start_index: i, target_index: min_index, mode: :min)
        end
        return array unless in_place
    end

    def max_one_directional(in_place: false)
        array = in_place ? @array : @array.clone
        n = array.size
        n.times do |i|
            max_index = n - i - 1
            search_and_swap(array, start_index: i, target_index: max_index, mode: :max)
        end
        return array unless in_place
    end

    private
    def search_and_swap(array, start_index:, target_index:, mode:)
        raise TypeError unless SORT_MODE.include? mode
        n = array.size
        case mode
        when :min
            (start_index..(n-1)).each { |j| target_index = j if array[j] < array[target_index] }
            array[start_index], array[target_index] = array[target_index], array[start_index]
        when :max
            (start_index..(n-1)).each { |j| target_index = n - j - 1 if array[n - j - 1] > array[target_index] }
            array[n - start_index - 1], array[target_index] = array[target_index], array[n - start_index - 1]
        else
            raise TypeError
        end
    end
end

target_array = (1..10).to_a.shuffle
puts target_array.inspect
test1 = target_array.clone
res1 = SelectionSorter.new(test1).min_one_directional
puts res1.inspect
test2 = target_array.clone
SelectionSorter.new(test2).min_one_directional(in_place: true)
puts test2.inspect
test3 = target_array.clone
res3 = SelectionSorter.new(test3).max_one_directional
puts res3.inspect
test4 = target_array.clone
SelectionSorter.new(test4).max_one_directional(in_place: true)
puts test4.inspect
