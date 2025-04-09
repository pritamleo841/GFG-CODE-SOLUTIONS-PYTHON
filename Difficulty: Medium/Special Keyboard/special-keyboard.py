#User function Template for python3

class Solution:
    def optimalKeys(self, N):
        '''
        At each i, try splitting:
            Use first j key presses to build up some 'A's
            Then use the rest to paste multiple times
        '''
        dp=[0]*(N+1)
        for i in range(1,N+1):
            # Default: just press 'A' i times
            dp[i]=dp[i-1]+1
            # Try all possible break points
            for j in range(1,i-2):
                dp[i]=max(dp[i],dp[j]*(i-j-1))
                #dp[j]: How many A’s you had after j key presses (before Ctrl-A)
                #(i-j-1): Number of Ctrl-Vs you can do after Ctrl-A and Ctrl-C
                #So you’re multiplying the content dp[j] by how many times it gets pasted
        return dp[N]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.optimalKeys(N))
        print("~")
# } Driver Code Ends