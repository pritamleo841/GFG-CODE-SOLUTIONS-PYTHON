#User function Template for python3
class Solution:
	def numOfWays(self, n, x):
	    '''
	    dp[j] += dp[j - i^x] → If you can form j - i^x, you can also form j by adding i^x
        You sum this up for all valid i where i^x <= n
	    '''
		dp=[0]*(n+1)
        dp[0]=1  # base case
        mod=10**9 + 7

        i=1
        while (i**x)<=n:
            y=i**x
            for j in range(n,y-1,-1):
                dp[j]=(dp[j]+dp[j-y])%mod
            i += 1

        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, x = input().split()
        n = int(n)
        x = int(x)
        ob = Solution()
        print(ob.numOfWays(n, x))
        print("~")

# } Driver Code Ends