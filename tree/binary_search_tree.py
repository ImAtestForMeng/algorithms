# Binary search tree in Python
# Depth-first: time complexity: O(n)
#              space complecity: O(h), h is the height of the tree
# Breadth-first:
#     time complexity: O(n)
#     space comlexity: O(1)-best; O(n)-worst

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.value == data:
            # Duplicate value are not allowed
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True
    
    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()
    
    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.value))
            if self.right_child:
                self.right_child.inorder()
                
    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.value))
    
            

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preorder(self):
        print("PreOrder")
        return self.root.preorder()

    def inorder(self):
        print("Inorder")
        return self.root.inorder()
    
    def postorder(self):
        print("Postorder")
        return self.root.postorder()
    
if __name__ == "__main__":
    bst = Tree()
    bst.insert(10)
    bst.insert(5)
    print(bst.insert(15))
    bst.preorder()
    bst.inorder()
    bst.postorder()
