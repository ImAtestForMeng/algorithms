class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        # add new node at the end of the linked list.
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        # print out the whole linked list
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
    
    def get(self, index):
        # print the index.th element
        if index >= self.length():
            print("ERROR: Get index out of range")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index: 
                print("Element at %dth is %d"%(cur_idx, cur.data))
                return cur.data
            cur_idx += 1
    
    def erase(self, index):
        # delete the index.th element
        if index >= self.length():
            print("ERROR: index out of range!")
            return
        
        cur_idx = 0
        cur = self.head
        while True:
            prev = cur
            cur = cur.next
            if cur_idx == index:
                prev.next = cur.next
                return
            cur_idx += 1
    
    def insert(self, data, index):
        # insert a node give data and index
        inserted_node = Node(data)
        cur = self.head
        cur_idx = 0

        if index >= self.length() or index < 0:
            print("ERROR: the index is out of range")
            return
        if index == 0 or index == (self.length() - 1):
            self.append(data)
            return
        else:
            while True:
                prev = cur
                cur = cur.next
                if cur_idx == index:
                    prev.next = inserted_node
                    inserted_node.next = cur
                    return
                cur_idx += 1


# test
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(3)
ll.append(9)
ll.display()
ll.get(1)
ll.erase(0)
ll.display()
ll.insert(data=1, index = 1)
ll.display()





