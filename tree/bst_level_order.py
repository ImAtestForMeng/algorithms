from queue import *
# Using built-in queue function

# time complexity: O(n)
# sapce complexity: O(1) -- best; O(n) -- worst, average 

# Get inspiration from here: https://blog.csdn.net/coder_orz/article/details/51363095
# from queue import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def level_order(node):
    q = Queue() # Using put(), get() for enque and deque
    
    # node is not None
    if node:
        q.put(node)
        while  not q.empty():
            current = q.get()
            print(current.value)
            if current.left_child != None: q.put(current.left_child)
            if current.right_child != None: q.put(current.right_child)

# Construct a binary tree
root  = Node(5)
root.left_child  = Node(3)
root.left_child.left_child  = Node(2)
root.left_child.right_child  = Node(4)
root.right_child  = Node(10)
root.right_child.left_child  = Node(6)
root.right_child.right_child  = Node(11)

level_order(root)
