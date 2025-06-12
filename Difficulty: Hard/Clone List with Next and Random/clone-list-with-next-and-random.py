# Link list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        #Interleave cloned nodes with original nodes
        curr=head
        while curr:
            new_node=Node(curr.data)
            new_node.next=curr.next
            curr.next=new_node
            curr=new_node.next
        #Assign random pointers to the cloned nodes
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next

        #Detach cloned list from original list
        dummy=Node(0)
        copy_curr=dummy
        curr=head
        while curr:
            copy_curr.next=curr.next
            curr.next=curr.next.next
            copy_curr=copy_curr.next
            curr=curr.next
        return dummy.next