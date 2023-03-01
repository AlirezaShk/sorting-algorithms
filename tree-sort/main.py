import random


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def fetch_children_asc(self, buffer) -> None:
        if self.left:
            self.left.fetch_children_asc(buffer)
        buffer.append(self.data)
        if self.right:
            self.right.fetch_children_asc(buffer)

class BST:
    def __init__(self):
        self.root = None

    def insert_val(self, val) -> None:
        if self.root is None: self.root = Node(val)
        else:
            parent_node = None
            node = self.root
            while(node is not None):
                parent_node = node
                if val > node.data:
                    node = node.right
                    child_dir = 'r'
                else:
                    node = node.left
                    child_dir = 'l'
            if child_dir == 'r': parent_node.right = Node(val)
            else: parent_node.left = Node(val)

    def fetch_ascending(self) -> list:
        res = []
        self.root.fetch_children_asc(buffer=res)
        return res


target_array = list(range(10))
random.shuffle(target_array)
print(target_array)
bst = BST()
for num in target_array:
    bst.insert_val(num)
print(bst.fetch_ascending())