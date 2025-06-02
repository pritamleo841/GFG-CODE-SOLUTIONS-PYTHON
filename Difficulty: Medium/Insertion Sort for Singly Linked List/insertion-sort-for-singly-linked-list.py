#User function Template for python3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None



class Solution:
    def insertionSort(self, head):
        if not head or not head.next:
            return head
        dummy=Node(0)
        curr=head
        while curr:
            prev=dummy
            next_node=curr.next
            #find the correct position to insert current in sorted part
            while prev.next and prev.next.data<curr.data:
                prev=prev.next
            #insert curr between prev and prev.next
            curr.next=prev.next
            prev.next=curr
            curr=next_node
        return dummy.next