'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
'''
1.We use a flag to indicate what relation we expect:
    flag = True: expect current.data <= current.next.data
    flag = False: expect current.data >= current.next.data
2.We traverse the list and:
3.Swap the data values of current and next nodes if the current relationship doesn’t match the expected one.
4.Toggle the flag after each pair.
'''
class Solution:
    def zigzag(self, head):
        if not head or not head.next:
            return head
        curr=head
        flag=True #indicates a <= b relationship
        while curr and curr.next:
            if flag:
                if curr.data>curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
            else:
                if curr.data<curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
            curr=curr.next
            flag=not flag
        return head
                