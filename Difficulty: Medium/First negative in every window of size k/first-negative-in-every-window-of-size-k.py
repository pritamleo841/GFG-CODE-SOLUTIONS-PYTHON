#User function Template for python3
from collections import deque
class Solution:
    #sliding window + queue (deque) problem
    def firstNegInt(self, arr, k): 
        n=len(arr)
        result=[]
        dq=deque()  # Store indices of negative numbers
        for i in range(n):
            # Remove out-of-window indices
            if dq and dq[0]<i-k+1:
                dq.popleft()
            # Add current index if negative
            if arr[i]<0:
                dq.append(i)
            #Store result once window of size k is hit
            if i>=k-1:
                result.append(arr[dq[0]] if dq else 0)
        return result
