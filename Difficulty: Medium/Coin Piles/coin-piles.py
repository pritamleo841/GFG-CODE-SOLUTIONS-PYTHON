#User function Template for python3
class Solution:
    def upperBound(self,arr,key):
        low,high=0,len(arr)-1
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]>key:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
    def minSteps(self, A, N, K):
       #Sort the array -O(nlogn)
        A.sort()
        # Build the prefix sum array
        prefix = [0] * N
        prefix[0] = A[0]
        for i in range(1, N):
            prefix[i] = prefix[i - 1] + A[i]
            
         # Initialize the minimum steps
        ans = float('inf')
        start = 0  # Track coins removed from smaller elements
        
        for i in range(N):
            # Calculate the permissible value
            permissible = A[i] + K

            # Find the upper bound index
            index = self.upperBound(A, permissible)
            if index == -1:  # If no upper bound is found
                index = N
                
            # Update `start` only when encountering a new unique element
            if i > 0 and A[i] != A[i - 1]:
                start = prefix[i - 1]

            # Compute the sum of remaining coins that need reduction
            if index == 0:
                actualSum = prefix[N - 1]  # No elements above `permissible`
            else:
                actualSum = prefix[N - 1] - prefix[index - 1]

            # Calculate the reduction for elements above `permissible`
            reduction = (N - index) * permissible
            actualSum -= reduction

            # Update the answer
            ans = min(ans, actualSum + start)
        return ans

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for _ in range (t):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    
    ob = Solution()
    print(ob.minSteps(A,N,K))
    print("~")
# } Driver Code Ends