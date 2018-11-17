# remove duplicate elements from linked list
# Write a removeDuplicates() function which takes a list and deletes
# any duplicate nodes from the list. The list is not sorted.

# For example if the linked list is 12->11->12->21->41->43->21,
# then removeDuplicates() should convert the list to 12->11->21->41->43.

# If temporary buffer is not allowed, how to solve it?

class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Solution_1:
    """
    两重循环删除重复节点，当前遍历节点作为第一重循环，当前节点的下一节点作为第二重循环

    @param head: A Node
    @return A Node
    time complexity: O(n^2)
    space complexity: O(1)
    """
    def deleteDuplicates(self, head):
        if head == None:
            return
        
        curr = head
        while curr is not None:
            inner = curr
            while inner.next is not None:
                if inner.next.value == curr.value:
                    inner.next = inner.next.next
                else:
                    inner = inner.next
            curr = curr.next
        return head
        
class Solution_2:
    """
    万能的哈希表

    @param head: A Node
    @return A Node
    time complexity: O(n)
    space complexity: O(n)
    """
    def  deleteDuplicates(self, head):
        if head is None:
            return None
        
        hash = {}
        hash[head.value] = True
        curr = head
        while curr.next is not None:
            if curr.next.value in hash:
                curr.next = curr.next.next
            else:
                hash[curr.next.value] = True
                curr = curr.next
        return head

        




