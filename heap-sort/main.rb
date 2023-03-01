# You'll need this gem: https://github.com/florian/rb_heap

def heap_sort(arr)
    Heap.sort(arr)
end


target_array = (1..10).to_a.shuffle
puts target_array.inspect
heap_sort(target_array)
puts target_array.inspect