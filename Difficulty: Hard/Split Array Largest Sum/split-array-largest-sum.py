#User function Template for python3

class Solution:
    #Painter's Partition Problem
    def splitArray(self, arr, N, K):
        # code here 
        def canSplit(largest):
            currSum=0
            subarray=1 #atleast one subarray is possible
            for n in arr:
                currSum+=n
                if currSum>largest:
                    subarray+=1 #new subarray needed
                    currSum=n #currSum in starting from n now
            return subarray<=K #if less than or equals to K subarrays possible
            
        #minimum sum will be max(arr), largest sum till now sum(arr)
        low,high = max(arr),sum(arr)
        res = high #largest sum possible till now
        
        while low<=high:
            mid = low+(high-low)//2
            if canSplit(mid):
                res=mid #new largest sum
                high=mid-1 #look for more smaller largest sum
            else:
                low=mid+1
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
        print("~")
# } Driver Code Ends