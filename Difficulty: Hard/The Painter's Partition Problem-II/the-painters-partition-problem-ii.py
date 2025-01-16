#User function Template for python3

class Solution:
    # code here 
    def canSplit(self,largest,K,arr):
        currSum=0
        subarray=1 #atleast one subarray is possible
        for n in arr:
            currSum+=n
            if currSum>largest:
                subarray+=1 #new subarray needed
                currSum=n #currSum in starting from n now
        return subarray<=K #if less than or equals to K subarrays possible
        
    def minTime (self, arr, k):
        #code here
        #minimum sum will be max(arr), largest sum till now sum(arr)
        low,high = max(arr),sum(arr)
        res = high #largest sum possible till now
        
        while low<=high:
            mid = low+(high-low)//2
            if self.canSplit(mid,k,arr):
                res=mid #new largest sum
                high=mid-1 #look for more smaller largest sum
            else:
                low=mid+1
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input())

        ob = Solution()
        print(ob.minTime(arr, k))

# } Driver Code Ends