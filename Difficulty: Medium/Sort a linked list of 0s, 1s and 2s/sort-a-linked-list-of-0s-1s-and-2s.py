'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def segregate(self, head):
        my_map={0:0,1:0,2:0}
        curr=head
        while curr:
            my_map[curr.data]+=1
            curr=curr.next
        dummy=Node(0)
        tail=dummy
        while my_map[0]:
            tail.next=Node(0)
            tail=tail.next
            my_map[0]=my_map[0]-1
        while my_map[1]:
            tail.next=Node(1)
            tail=tail.next
            my_map[1]=my_map[1]-1
        while my_map[2]:
            tail.next=Node(2)
            tail=tail.next
            my_map[2]=my_map[2]-1
        return dummy.next
        
    