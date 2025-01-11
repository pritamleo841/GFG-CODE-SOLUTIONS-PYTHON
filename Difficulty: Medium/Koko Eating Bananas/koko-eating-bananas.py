#User function Template for python3
import math
class Solution:
    def kokoEat(self,arr,k):
        # Code here
        #binary search solution - O(log(max(arr)).len(arr))
        low,high=1,max(arr)
        res = high #Max koko can eat
        while low<=high:
            mid = low+(high-low)//2
            hours=0
            for p in arr:
                hours+=math.ceil(p/mid)
            
            if hours<=k:
                res=min(res,mid)
                high=mid-1
            else:
                low=mid+1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kokoEat(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends