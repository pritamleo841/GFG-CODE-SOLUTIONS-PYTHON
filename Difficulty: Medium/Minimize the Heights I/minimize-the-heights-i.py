#User function Template for python3

class Solution:
    def getMinDiff(self,arr,k):
        '''
        Step-by-step approach-
            1. Sort the array
            Sorting helps us deal with towers in ascending order and make decisions about raising or lowering heights systematically.
            
            2. Initial difference
            The naive difference before any change = arr[-1] - arr[0].
            
            3. Modify potential extremes
            After increasing the smallest element by k and decreasing the largest element by k, the middle elements may still break the minimal range if not handled carefully.
            
            4. Idea
            For each index i from 0 to n-2:
                Imagine arr[0] + k could be the new minimum, but also arr[i+1] - k could be the new minimum if we reduce taller ones.
                Similarly, arr[i] + k could be the new maximum, but also arr[-1] - k could be the new maximum.
                
                We check min height = min(arr[0] + k, arr[i+1] - k)
                and max height = max(arr[i] + k, arr[-1] - k).
            
            5. Pick the smallest possible difference
        '''
       
        arr.sort()
        diff = arr[-1] - arr[0]
        
        for i in range(len(arr) - 1):
            lower = min(arr[0] + k, arr[i + 1] - k)
            upper = max(arr[-1] - k, arr[i] + k)
            diff = min(diff, upper - lower)
        
        return diff
        
        