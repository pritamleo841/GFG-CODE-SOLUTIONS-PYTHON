#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        '''
        To reverse a stack recursively:
            1. Pop the top element.
            2. Recursively reverse the remaining stack.
            3. Insert the popped element at the bottom of the stack.
        '''
        def insert_at_bottom(stack,element):
            if not stack:
                stack.append(element)
                return
            else:
                temp = stack.pop()
                insert_at_bottom(stack,element)
                stack.append(temp)
        if St:
            temp = St.pop()
            self.reverse(St)
            insert_at_bottom(St,temp)
            
            
            


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
    print("~")
# } Driver Code Ends