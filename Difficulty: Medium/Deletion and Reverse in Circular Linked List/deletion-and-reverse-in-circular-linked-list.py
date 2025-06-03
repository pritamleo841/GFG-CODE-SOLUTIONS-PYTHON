'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next==head:
            return head
        stop=head
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            if curr==stop:
                break
        head.next=prev
        head=prev
        return head
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if not head:
            return None
        #when single node but key is head
        if head.data==key and head.next==head:
            head=None
            return head
        #when multiple node but key is head
        if head.data==key:
            last=head
            while last.next!=head:
                last=last.next
            last.next=head.next
            head=head.next
            return head
        #when key is at middle
        curr=stop=head
        prev=None
        while True:
            prev=curr
            curr=curr.next
            if curr.data==key:
                prev.next=curr.next
                return head
            if curr==stop:
                break #full circle, not found
        
        return head
            
        