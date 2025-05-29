class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    '''
    1.Traverse the list.
    2.Whenever you find a negative number, move it to the front of the list.
    3.Leave positive numbers in place.
    4.This works because the list is already sorted by absolute values 
    — so negative numbers appear in reverse order
    '''
    def sortList(self, head):
        # Initialize previous and  current nodes 
        prev = head 
        curr = head.next
        # Traverse list 
        while(curr != None): 
            # If curr is smaller than prev,then it must be moved to head 
            if(curr.data < prev.data):
                # Detach curr from linked list 
                prev.next = curr.next
                # Move current node to beginning 
                curr.next = head 
                head = curr
                # Update current 
                curr = prev
            # Nothing to do if current element is at right place 
            else:
                prev = curr
            # Move current 
            curr = curr.next
        return head 