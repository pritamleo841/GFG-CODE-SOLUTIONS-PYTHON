
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


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
    
    def merge(self,l1,l2):
        dummy=Node(0)
        tail=dummy
        while l1 and l2:
            if l1.data<l2.data:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return dummy.next
        
    def sort(self, head):
        if not head or not head.next:
            return head
        asc_dummy=Node(0)
        desc_dummy=Node(0)
        asc_list=asc_dummy
        desc_list=desc_dummy
        is_odd=True
        curr=head
        while curr:
            if is_odd:
                asc_list.next=curr
                asc_list=asc_list.next
            else:
                desc_list.next=curr
                desc_list=desc_list.next
            curr=curr.next
            is_odd = not is_odd
        asc_list.next = None
        desc_list.next = None
        return self.merge(asc_dummy.next,self.reverse(desc_dummy.next))
        