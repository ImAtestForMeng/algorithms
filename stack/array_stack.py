class Stack:
    def __init__(self):
        self._a = []
    def push(self, item):
        self._a += [item]
    def pop(self):
        return self._a.pop()
    def isEmpty(self):
        return len(self._a) == 0
    def __str__(self):
        s = ''
        for item in reversed(self._a):
            s = str(item)+ ' ' + s
        return s 


# stack = Stack()
# stack.push(1)
# stack.push(3)
# stack.push(2)
# stack.push(6)
# print(stack)



