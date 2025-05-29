''' Node for linked list:
'''
class Node:
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
        
    def addTwoLists(self, num1, num2):
        ptr1=self.reverse(num1)
        ptr2=self.reverse(num2)
        dummy=Node(0)
        tail=dummy
        curry=0
        while ptr1 or ptr2 or curry:
            total_sum = (
                (ptr1.data if ptr1 else 0)+
                (ptr2.data if ptr2 else 0)+
                curry)
                
            curry=total_sum//10
            digit=total_sum%10
               
            tail.next = Node(digit)
            tail=tail.next
            if ptr1:ptr1=ptr1.next
            if ptr2:ptr2=ptr2.next
            
        result = self.reverse(dummy.next)
        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next
        
        return result   
                
                
                
                
                
                
            