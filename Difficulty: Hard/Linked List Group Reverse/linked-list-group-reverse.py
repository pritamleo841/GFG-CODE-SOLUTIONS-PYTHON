"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    '''
    1.Traverse k nodes and reverse them.
    2.Recursively reverse the next part of the list.
    3.Connect the reversed part to the recursively reversed rest.
    4.If fewer than k nodes are left, still reverse them.
    '''
    def reverseKGroup(self, head, k):
        prev = None
        current = head
        nnext = None
        count = 0
        # Reverse k nodes
        while current and count < k:
            nnext = current.next
            current.next = prev
            prev = current
            current = nnext
            count += 1
        # Recursively reverse the next part and attach
        if current:
            head.next = self.reverseKGroup(current, k)
        # 'prev' is the new head after reversing k nodes
        return prev
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            