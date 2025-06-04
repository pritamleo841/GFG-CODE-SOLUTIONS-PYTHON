'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head or not head.next:
            return head
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else: #while can be used with else statement in python(wow fact!!!)
            return head
        slow=head
        if slow==fast:
            #loop at head
            while fast.next!=slow:
                fast=fast.next
        else:
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next
        fast.next=None #break
        return head