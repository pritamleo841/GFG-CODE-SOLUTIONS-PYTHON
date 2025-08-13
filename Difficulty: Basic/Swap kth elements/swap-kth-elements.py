
class Solution:
    def swapKth(self, arr, k):
        n=len(arr)
        start_index=k-1           # kth from start (0-based)
        end_index=n-k             # kth from end (0-based)
        
        arr[start_index],arr[end_index]=arr[end_index],arr[start_index]
        return arr
        
