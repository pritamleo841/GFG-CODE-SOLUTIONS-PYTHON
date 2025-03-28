#User function Template for python3
class Solution:
    def numberOfPath (self, n, k, arr):
        # DP Table: dp[i][j][sum_k] -> # of ways to reach (i, j) with sum_k coins
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
        # Base Case: Start at (0, 0) with arr[0][0] coins
        if arr[0][0] <= k:
            dp[0][0][arr[0][0]] = 1
    
        # Fill the DP table
        for i in range(n):
            for j in range(n):
                for sum_k in range(k + 1):
                    if dp[i][j][sum_k] > 0:  # If there are ways to reach (i, j) with sum_k
                        # Move Down
                        if i + 1 < n and sum_k + arr[i + 1][j] <= k:
                            dp[i + 1][j][sum_k + arr[i + 1][j]] += dp[i][j][sum_k]
                        
                        # Move Right
                        if j + 1 < n and sum_k + arr[i][j + 1] <= k:
                            dp[i][j + 1][sum_k + arr[i][j + 1]] += dp[i][j][sum_k]
    
        # Result: Ways to reach (n-1, m-1) with exactly k coins
        return dp[n-1][n-1][k]
        ''''
        directions = [(1,0),(0,1)]
        
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<n
            
        def dfs(r,c,sum_k):
            if sum_k>k:
                return 0
            sum_k+=arr[r][c]
            if r==n-1 and c==n-1:
                return 1 if sum_k==k else 0
            count=0
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if isInBoundary(nr,nc):
                    count+=dfs(nr,nc,sum_k)
            return count
        return dfs(0,0,0)
        '''



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


        print("~")
# } Driver Code Ends