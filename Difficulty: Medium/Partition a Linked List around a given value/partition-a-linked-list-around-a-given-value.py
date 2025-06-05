#User function Template for python3


class Node:
    def __init__(self, data):
		self.data = data
		self.next = None


class Solution:
    def concat(self,l_head,e_head,g_head):
        head=tail=None
        for part in [l_head,e_head,g_head]:
            if not part:
                continue
            if not head:
                head=tail=part
            else:
                tail.next=part
            while tail.next:
                tail=tail.next
        return head
        
    def partition(self, head, x):
        if not head or not head.next:
            return head
        pivot=x
        l_dummy=Node(0)
        e_dummy=Node(0)
        g_dummy=Node(0)
        l_tail=l_dummy
        e_tail=e_dummy
        g_tail=g_dummy
        curr=head
        while curr:
            next_node=curr.next
            curr.next=None
            if curr.data<pivot:
                l_tail.next=curr
                l_tail=curr
            elif curr.data>pivot:
                g_tail.next=curr
                g_tail=curr
            else:
                e_tail.next=curr
                e_tail=curr
            curr=next_node
        l_tail=None
        e_tail=None
        g_tail=None
        return self.concat(l_dummy.next,e_dummy.next,g_dummy.next)