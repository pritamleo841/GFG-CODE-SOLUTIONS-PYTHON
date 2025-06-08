'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''Algorithm-
1.Count the total number of nodes n.
2.If k > n, return the list as is.
3.If 2k - 1 == n, it's the same node (no swap needed).
4.Find:
    prevX and X (kth node from beginning)
    prevY and Y (kth node from end)
5.Swap their links correctly, taking care of corner cases like head swaps or adjacent nodes.
'''
class Solution:
    def swap_kth_node(self, head, k):
        if not head or not head.next:
            return head
        
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next
        if ((k>n) or (2*k-1==n)):
            return head
        #find kth node from beginning and its previous
        prevX=None
        X=head
        for _ in range(k-1):
            prevX=X
            X=X.next
        #find kth node from end and its previous
        prevY=None
        Y=head
        for _ in range(n-k):
            prevY=Y
            Y=Y.next
        #adjusting conntecing nodes and check for head condition
        if prevX:
            prevX.next=Y
        else:
            head=Y
        if prevY:
            prevY.next=X
        else:
            head=X
        #swap next pointers
        X.next,Y.next=Y.next,X.next
        return head
        
        
        
        
        
        
        
        
        
        
        