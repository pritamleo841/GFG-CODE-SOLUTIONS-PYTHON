

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
            
    def addOne(self,head):
        carry=1
        rev_head = self.reverse(head)
        curr=rev_head
        prev=None
        while curr:
            total_sum = curr.data + carry
            digit=total_sum%10
            carry=total_sum//10
            curr.data=digit
            prev=curr
            curr=curr.next
        if carry:
            prev.next=Node(carry)
        return self.reverse(rev_head)
        