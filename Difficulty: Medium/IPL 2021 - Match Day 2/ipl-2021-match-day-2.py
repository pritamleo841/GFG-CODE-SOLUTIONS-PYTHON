#User function Template for python3

from collections import deque
class Solution:
    def max_of_subarrays(self, arr, n, K):
        '''
        Core Idea:
        We maintain a deque of indices where elements are in decreasing order of values.
        For each index i, we:
        Pop from the back of the deque if arr[i] is greater than or equal to arr[deque[-1]].
        Pop from the front if it's out of the current window.
        Push current index i.
        If window is fully formed (i ≥ K - 1), append arr[deque[0]] to result (max of current window).
        '''
        result=[]
        dq=deque() #store indices
        for i in range(n):
            #Remove indices out of this window
            while dq and dq[0]<=i-K:
                dq.popleft()
            #Remove smaller values from the end
            while dq and arr[i]>=arr[dq[-1]]:
                dq.pop()
            #Add current index
            dq.append(i)
            #Append max of window to result
            if i>=K-1:
                result.append(arr[dq[0]])
    
        return result
        
            
            
