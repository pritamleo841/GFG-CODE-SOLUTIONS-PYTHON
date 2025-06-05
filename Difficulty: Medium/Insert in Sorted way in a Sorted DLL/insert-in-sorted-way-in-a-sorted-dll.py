
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        new_node = Node(x)
        # Case 1: Insert at beginning or before head
        if not head:
            return new_node
        if x<=head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        # Traverse to find the position
        curr = head
        while curr.next and curr.data<x:
            curr = curr.next
        if curr.data < x:
            # Insert at end
            curr.next = new_node
            new_node.prev = curr
        else:
            # Insert before curr
            prev = curr.prev
            prev.next = new_node
            new_node.prev = prev
            new_node.next = curr
            curr.prev = new_node

        return head
            