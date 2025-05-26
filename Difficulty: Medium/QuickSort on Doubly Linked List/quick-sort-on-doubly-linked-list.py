
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def concat(self,less,equal,great):
        dummy=DLLNode(0)
        tail=dummy
        
        def attach(node):
            nonlocal tail
            while node:
                tail.next=node
                tail.prev=tail
                tail=tail.next
                node=node.next
                
        attach(less)
        attach(equal)
        attach(great)
        tail.next=None
        return dummy.next
            
    def quick_sort(self, head):
        if not head or not head.next:
            return head
        less_dummy=DLLNode(0)
        equal_dummy=DLLNode(0)
        great_dummy=DLLNode(0)
        #always terminate sublists
        less_tail=less_dummy
        equal_tail=equal_dummy
        great_tail=great_dummy
        pivot=head
        curr=head
        while curr:
            next_node=curr.next  # Save next because we will break links
            curr.prev=curr.next=None  # Isolate the node
            if curr.data<pivot.data:
                less_tail.next=curr
                curr.prev=less_tail
                less_tail=curr
            elif curr.data==pivot.data:
                equal_tail.next=curr
                curr.prev=equal_tail
                equal_tail=curr
            else:
                great_tail.next=curr
                curr.prev=great_tail
                great_tail=curr
            curr=next_node

        sorted_less=self.quick_sort(less_dummy.next)
        sorted_great=self.quick_sort(great_dummy.next)

        return self.concat(sorted_less,equal_dummy.next,sorted_great)
            