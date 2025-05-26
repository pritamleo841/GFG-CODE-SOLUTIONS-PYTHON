'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            #loop detected
            if slow==fast:
                return True
        return False
        # slow=head
        # count=1
        # while slow!=fast:
        #     slow=slow.next
        #     fast=fast.next
        #     count+=1
        # return count