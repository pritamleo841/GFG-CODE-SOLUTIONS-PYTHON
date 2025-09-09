#User function Template for python3

class Solution:
    def longest(self, arr):
        #Code Here
        stack=[arr[0]]
        for i in range(1,len(arr)):
            if arr[i]>=stack[-1]:
                stack.append(arr[i])
        return len(stack)
