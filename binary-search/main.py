class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def create_from_array(arr: list):
        # Median element is just a random choice, so that if the
        #  array is semi-sorted, we won't be stuck in the
        #  worst case searching time complexity
        median = len(arr) // 2
        bst = BST(root=arr.pop(median))
        for el in arr:
            bst.insert(el)
        return bst

    def insert(self, new_val):
        node = self.root
        parent = None
        while node is not None:
            parent = node
            if node.value >= new_val:
                node = node.left
            else:
                node = node.right
        if parent.value > new_val:
            parent.left = Node(new_val)
        else:
            parent.right = Node(new_val)

    def search(self, find_val):
        node = self.root
        while node is not None:
            if node.value == find_val:
                return True
            elif node.value > find_val:
                node = node.left
            else:
                node = node.right
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))


arr = [1, 100, -5, -72, 85, 31, -52, 49, -37]
print(sorted(arr))
bst = BST.create_from_array(arr)
print(bst.search(85))
