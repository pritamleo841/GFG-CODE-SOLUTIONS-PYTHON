class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        

'''
🔒 Rule of Thumb:
Whenever you're breaking and rebuilding linked lists 
(partitioning, reversing, merging), always disconnect each node's .next 
unless you're absolutely sure of the structure and final links.
'''
class Solution:
    def merge(self,a,b):
        if not a :
            return b
        if not b :
            return a
        if a.data<b.data:
            result=a
            result.bottom=self.merge(a.bottom,b)
        else:
            result=b
            result.bottom=self.merge(a,b.bottom)
        result.next=None
        return result
            
    def flatten(self, root):
        if not root or not root.next:
            return root
        #recur list from left to right
        root.next=self.flatten(root.next)
        #merge this list with the right one
        root=self.merge(root,root.next)
        return root
        
            
        