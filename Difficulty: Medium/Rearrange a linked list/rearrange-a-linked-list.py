
# Linked List Node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.next = None
		
class Solution:    
    def rearrangeEvenOdd(self, head):
        even_dummy=Node(0)
        odd_dummy=Node(0)
        tail_e = even_dummy
        tail_o = odd_dummy
        curr=head
        is_odd = True
        while curr:
            next_node=curr.next #save next node of curr in advance
            curr.next=None #disconnect to avoid loop
            if is_odd:
                tail_o.next=curr
                tail_o=tail_o.next
            else:
                tail_e.next=curr
                tail_e=tail_e.next
            curr=next_node #vital step here
            is_odd=not is_odd
            
        tail_o.next=even_dummy.next #connect 
        return odd_dummy.next
        
        