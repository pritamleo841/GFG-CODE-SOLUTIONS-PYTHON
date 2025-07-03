class Solution:
    def nextLargerElement(self, arr):
        #We can simulate circular behavior by iterating twice over the array(2×n),
        #while using a stack to keep track of potential next greater elements.
        n=len(arr)
        result=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            curr_index=i%n
            current=arr[curr_index]
            #Pop all smaller or equal elements from stack
            while stack and arr[stack[-1]]<=current:
                stack.pop()
            #If within first pass (actual indices), update result
            if i<n:
                if stack:
                    result[curr_index]=arr[stack[-1]]
            stack.append(curr_index)
        return result