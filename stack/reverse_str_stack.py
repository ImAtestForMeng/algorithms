""" 
reverse string using array Stack
method 1: time: O(n), space: O(n)
method 2: time: O(n), space: O(1)
""" 
from array_stack import Stack
# reverse string using linked stack
from linkedlist_stack import Stack as LLStack
from linkedlist_stack import _Node

input_str = "no matter what"

""" 
method 1
"""
stack = Stack()
for char in input_str:
    stack.push(char)
while not stack.isEmpty():
    print(stack.pop())

"""
method 2
"""
def reverse(string):
    return string[::-1]

print(reverse(input_str))

#-----------------------------------------------------------------------
""" 
reverse string using linked list Stack
time: O(n), space: O(n)
""" 
ll_stack = LLStack()

for char in input_str:
    ll_stack.push(char)
while not ll_stack._first:
    print(ll_stack.pop())