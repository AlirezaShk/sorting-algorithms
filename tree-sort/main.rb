class Node
    def initialize data:
        @data = data
    end

    def fetch_children_asc buffer:
        left&.fetch_children_asc(buffer: buffer)
        buffer << data
        right&.fetch_children_asc(buffer: buffer)
    end

    attr_accessor :data, :left, :right
end

class BST
    def insert_val val
        if root.nil?
            @root = Node.new(data: val)
        else
            parent_node = child_dir = nil
            node = root
            until node.nil?
                parent_node = node
                if val > node.data
                    node = node.right
                    child_dir = 'r'
                else
                    node = node.left
                    child_dir = 'l'
                end
            end
            if child_dir == 'l'
                parent_node.left = Node.new(data: val)
            else
                parent_node.right = Node.new(data: val)
            end
        end
    end

    def fetch_ascending
        res = []
        root.fetch_children_asc buffer: res
        res
    end

    attr_accessor :root
end


target_array = (1..10).to_a.shuffle
puts target_array.inspect
bst = BST.new
target_array.each { |num| bst.insert_val num }
puts bst.fetch_ascending.inspect