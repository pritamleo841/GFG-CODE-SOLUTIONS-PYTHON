
#   reverse alternate nodes and append at the end
#   The input list will have at least one element
#   Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
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
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        head = l1
        while l1.next:
            l1 = l1.next
        l1.next = l2
        return head
            
    def rearrange(self, head):
        if not head or not head.next:
            return head
            
        dummy_odd = Node(0)
        dummy_even = Node(0)
        tail_odd = dummy_odd
        tail_even = dummy_even

        curr = head
        is_even = False

        while curr:
            next_node = curr.next  # Save next before breaking
            curr.next = None       # Important to avoid link corruption
            if is_even:
                tail_even.next = curr
                tail_even = tail_even.next
            else:
                tail_odd.next = curr
                tail_odd = tail_odd.next
            curr = next_node
            is_even = not is_even
            
        # Reverse the even-positioned list
        reversed_even = self.reverse(dummy_even.next)

        # Merge odd list and reversed even list
        return self.merge(dummy_odd.next, reversed_even)
        
            
            
            
            
            
            
            
            