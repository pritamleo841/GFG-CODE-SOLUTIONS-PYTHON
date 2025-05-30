# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        if k==0 or not head:
            return head
            
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
            
        k=k%length
        if k==0:
            return head
        curr=head    
        for _ in range(k-1): #till kth node
            curr=curr.next
            
        new_head=curr.next
        curr.next=None
        
        tail.next=head
        return new_head