'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
#Function to check whether the list is palindrome.
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
        
    def isIdentical(self,l1,l2):
        while l1 and l2:
            if l1.data!=l2.data:
                return False
            l1=l1.next
            l2=l2.next
        return l1 is None and l2 is None
        
    def clone(self,head):
        if not head:
            return None
        new_head=Node(head.data)
        curr_orig=head.next
        curr_clone=new_head
        while curr_orig:
            curr_clone.next=Node(curr_orig.data)
            curr_orig=curr_orig.next
            curr_clone=curr_clone.next
        return new_head
    
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        cloned_head=self.clone(head)
        reversed_cloned=self.reverse(cloned_head)
        return self.isIdentical(head,reversed_cloned)