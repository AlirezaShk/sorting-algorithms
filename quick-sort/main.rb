# This is an ascending sorter based on Quick Sort
class AscQuickSorter
    def initialize array
        @subject = array
    end

    def run begin_: 0, end_: nil
        # initialize end index for first run
        end_ = subject.size - 1 if end_.nil?
        # make sure iteration loop is limited
        return subject unless begin_ < end_

        # find pivot element
        pivot = find_pivot(begin_: begin_, end_: end_)
        # sort a partition and retrieve the partition border
        index = sort_partition_by_pivot(pivot: pivot, begin_: begin_, end_: end_)
        # iterate the process for the higher and lower partitions
        run(begin_: begin_, end_: index - 1)
        run(begin_: index + 1, end_: end_)
    end

    private
    attr_accessor :subject
    # We're considering the last element as pivot
    def find_pivot begin_:, end_:
        subject[begin_..end_][-1]
    end

    def sort_partition_by_pivot pivot:, begin_:, end_:
        # we're on an ascending order so the first eligible position for filling is the start of partition
        next_eligible_pos = begin_
        # iterate through each element of the partition
        (begin_..end_-1).to_a.each do |i|
            # is the pivot greater than the element?
            if pivot >= subject[i]
                # fill the eligible position with the target element
                @subject[i], @subject[next_eligible_pos] = subject[next_eligible_pos], subject[i]
                # move the eligible position cursor one step
                next_eligible_pos += 1
            end
        end
        
        # all the lower elements have been filling the positions from starting point
        #  now we have to swap the pivot element to the next eligible positon
        @subject[end_], @subject[next_eligible_pos] = subject[next_eligible_pos], subject[end_]
        # return the pivot's right (new) position
        next_eligible_pos
    end
end

target_array = (1..10).to_a.shuffle
puts target_array.inspect
res = AscQuickSorter.new(target_array).run()
puts res.inspect

