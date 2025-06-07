#User function Template for python3

class Solution:
    def modify_the_list(self, head):
        if not head or not head.next:
            return head
            
        values=[]
        curr=head
        while curr:
            values.append(curr.data)
            curr=curr.next
        n=len(values)
        first_half=values[:n//2]
        #condition 1
        curr=head
        for i in range(n//2):
            curr.data=values[n-1-i]-curr.data
            curr=curr.next
        #condition 3   
        if n%2:
            curr=curr.next
        #condition 2    
        for val in first_half[::-1]:
            curr.data=val
            curr=curr.next
        return head
            