class Stack:
    def __init__(self):
        self._first = None  # Reference to first _Node

    def isEmpty(self):
        return self._first is None
    def push(self, item):
        # It's the opposite of inserting element to a listed list
        self._first = _Node(item, self._first)

    def pop(self):
        item = self._first.item
        self._first = self._first.next
        return item

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s

#-----------------------------------------------------------------------

# A _Node object references an item and a next _Node object.
# A Stack object is composed of _Node objects.

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item.
        self.next = next  # Reference to the next _Node object

#-----------------------------------------------------------------------

# test_stack = Stack()
# test_stack.push(1)
# test_stack.push(2)
# test_stack.push(3)
# test_stack.push(4)
# test_stack.push(5)
# print(test_stack)