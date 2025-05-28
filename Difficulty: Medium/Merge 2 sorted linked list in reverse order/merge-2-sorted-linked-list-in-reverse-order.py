
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def mergeResult(self, node1, node2):
        result=None
        ptr1=node1
        ptr2=node2
        while ptr1 and ptr2:
            if ptr1.data<=ptr2.data:
                temp=ptr1
                ptr1=ptr1.next
            else:
                temp=ptr2
                ptr2=ptr2.next
            temp.next=result #insert at head
            result=temp
        while ptr1:
            temp=ptr1
            ptr1=ptr1.next
            temp.next=result
            result=temp
        while ptr2:
            temp=ptr2
            ptr2=ptr2.next
            temp.next=result
            result=temp
        return result
            