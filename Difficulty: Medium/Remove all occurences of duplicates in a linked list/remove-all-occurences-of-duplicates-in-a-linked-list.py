#User function Template for python3


# Linked list Node class

class Node :
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def removeAllDuplicates(self, head):
        if not head or not head.next:
            return head
            
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.data == curr.next.data:
                # Skip all duplicates
                while curr.next and curr.data == curr.next.data:
                    curr = curr.next
                curr = curr.next  # Skip the last duplicate
                prev.next = curr  # Remove all duplicates
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next
        
        
        