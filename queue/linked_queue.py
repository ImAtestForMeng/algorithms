class _Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self._first = None # Reference to first _Node
        self._last = None # Reference to last _Node
        self._length= 0 # Length of items

    def isEmpty(self):
        return self._first is None
    
    # Add item to the end of self
    def enqueue(self, item):
        old_last = self._last
        self._last = _Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            old_last.next = self._last
        self._length += 1

    # Remove the first item of self and return it
    def dequeue(self):
        item  = self._first.item
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        self._length -= 1
        return item

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.isEmpty())
print(queue.dequeue())



        
