#User function Template for python3


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def reverseBetween(self, a, b, head):
        if not head or a==b:
            return head

        dummy=Node(0)
        dummy.next=head
        prev=dummy
    
        #Reach node at position a
        for _ in range(a-1):
            prev=prev.next
        start_prev=prev
        start=prev.next
    
        #Reverse from a to b
        curr=start
        prev=None
        for _ in range(b - a + 1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
    
        #Connect reversed part
        start_prev.next=prev       # prev is now the new head of reversed sublist
        start.next=curr            # start is now the tail of reversed sublist
    
        return dummy.next
        
        
            
        
        