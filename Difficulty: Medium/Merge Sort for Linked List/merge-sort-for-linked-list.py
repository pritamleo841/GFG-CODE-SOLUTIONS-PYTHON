#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def split(self,head):
        fast = head
        slow = head
        # Move fast pointer two steps and slow pointer
        # one step until fast reaches the end
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        # Split the list into two halves
        second = slow.next
        slow.next = None
        return second
    
    def merge(self,first, second):
        # If either list is empty, return the other list
        if not first:
            return second
        if not second:
            return first
        # Pick the smaller value between first and second nodes
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second
    
    def merge_sort(self,head):
        # Base case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head
        # Split the list into two halves
        second = self.split(head)
        # Recursively sort each half
        head = self.merge_sort(head)
        second = self.merge_sort(second)
        # Merge the two sorted halves
        return self.merge(head, second)

        
    def mergeSort(self, head):
        return self.merge_sort(head)
        