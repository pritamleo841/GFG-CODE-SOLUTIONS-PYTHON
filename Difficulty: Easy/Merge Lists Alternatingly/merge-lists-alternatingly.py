'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

''' your task is to complete this function
    function should return a list of the two new heads
'''
class Solution:
    def merge_list(self, head1, head2):
        curr1=head1
        curr2=head2
        while curr1 and curr2:
            #take next pointers
            next1=curr1.next
            next2=curr2.next
            #insert curr2 after curr1
            curr1.next=curr2
            curr2.next=next1
            #move pointers
            curr1=next1
            curr2=next2
        return [head1,curr2] #head2 remaining nodes into curr2