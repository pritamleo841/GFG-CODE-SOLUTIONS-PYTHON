#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        #binary search - O(logn)
        low,high=0,len(arr)-1
        result=-1
    
        while low<=high:
            mid=(low+high) // 2
    
            if arr[mid]==1:
                result=mid       # potential answer
                high=mid - 1     # search left half for earlier 1
            else:
                low=mid + 1      # search right half for 1's
    
        return result
    

