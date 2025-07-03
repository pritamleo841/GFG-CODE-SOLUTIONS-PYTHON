class Solution:
    def nextLargerElement(self, arr):
        #monotonic increasing stack
        n=len(arr)
        stack=[]
        result=[-1]*n
        for i in range(n-1,-1,-1):
            current=arr[i]
            #pop from stack until stack top<=current elem
            while stack and stack[-1]<=current:
                stack.pop()
            #after popping if stills elem in stack ,then that is next greater elem
            if stack:
                result[i]=stack[-1]
            stack.append(current)
        return result
            
        