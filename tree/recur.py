class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def insert(node, key):
    # Base case
    if node is None:
        return Node(key)

    # Recursion
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    return node

tree = Node(1)
tree = insert(tree, 2)
tree = insert(tree, 3)
tree = insert(tree, 6)
tree = insert(tree, 0)

print(tree.right.value)