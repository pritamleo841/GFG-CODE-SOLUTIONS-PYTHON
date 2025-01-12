#User function Template for python3

class Solution:
    def daysRequiredWithCapacity(self,arr,days,capacity):
        load=0
        days=1
        n=len(arr)
        for i in range(n):
            if load+arr[i]>capacity:
                days+=1
                load=arr[i]
            else:
                load+=arr[i]
        return days
        
    def leastWeightCapacity(self, arr, n, d):
        # code here 
        #range of capacity [max(arr)....sum(arr)]
        low,high = max(arr),sum(arr)
        ans=-1
        while low<=high :
            mid=low+(high-low)//2
            daysReq = self.daysRequiredWithCapacity(arr,d,mid)
            
            if daysReq<=d:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))
        D = int(input())

        ob = Solution()
        print(ob.leastWeightCapacity(arr, N, D))

# } Driver Code Ends