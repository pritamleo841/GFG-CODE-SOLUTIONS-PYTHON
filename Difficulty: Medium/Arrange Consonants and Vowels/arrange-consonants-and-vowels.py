
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        dummy=Node(0)
        dummy1=Node(0)
        tail=dummy
        tail1=dummy1
        curr=head
        while curr:
            next_node=curr.next
            curr.next=None #breaking new nodes in necessary to avoid loops
            if curr.data in ('a','e','i','o','u'): #vowels
                tail.next=curr
                tail=tail.next
            else:
                tail1.next=curr
                tail1=tail1.next
            curr=next_node
        tail.next=dummy1.next
        return dummy.next
        