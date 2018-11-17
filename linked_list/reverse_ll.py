class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
def reverse_llist(llist):
    # time cpmlexity: O(n)

    previous = None
    current = llist.head
    if current is None:
        return
    after = current.next
    while after:
        current.next = previous
        previous = current
        current = after
        after = after.next # reason why you shold initilize head.next = None
    current.next = previous
    llist.head = current

a_llist = LinkedList()
 
data_list = [1,2,3,4,5,6]
for data in data_list:
    a_llist.append(int(data))
 
reverse_llist(a_llist)
 
print('The reversed list: ')
a_llist.display()
