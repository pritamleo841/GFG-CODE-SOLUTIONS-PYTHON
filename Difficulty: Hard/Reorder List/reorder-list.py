'''
# Node Class
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''


#Back-end complete function Template for Python 3
'''
1.Find the middle of the list.
2.Reverse the second half of the list.
3.Merge the two halves alternately.
'''
class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    def reorderList(self, head):
        if not head or not head.next:
            return head
        #Find middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #Reverse second half
        second=self.reverse(slow.next)
        slow.next=None  # split the list

        #Merge two halves
        first=head
        while second:
            tmp1=first.next
            tmp2=second.next

            first.next=second
            second.next=tmp1

            first=tmp1
            second=tmp2
        return head
    
        
            
            
            
            