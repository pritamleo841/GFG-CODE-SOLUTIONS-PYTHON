class Solution:
    def calculateSpan(self, arr):
        #Problem Statement -
        #How many consecutive days (ending at today) has the price been ≤ today's price?
        
        #Monotonic (Decreasing) Stack O(n)
        stack=[]
        span=[0]*len(arr)
        for i in range(len(arr)):
            #Pop all elements from top where stack top<=current elemebt
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            #If stack is empty,span is i+1
            span[i]=i+1 if not stack else i-stack[-1] #Distance from last higher price
            #Push this element’s index into stack
            stack.append(i)
        return span
        
        '''
        #Naive approach O(n**2)
        n=len(arr)
        span=[0]*n
        for i in range(n):
            span[i]=1
            j=i-1 #check from i-1 to beginning for consecutive days
            while j>=0 and arr[j]<=arr[i]:
                span[i]+=1
                j-=1
        return span
        '''