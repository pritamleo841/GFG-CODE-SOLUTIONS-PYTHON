#User function Template for python3

class Solution:
    def fill(self,  mat):
        # code here
        n,m = len(mat),len(mat[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<m
        
        def dfs(r, c):
            mat[r][c] = 'M'  # Mark as visited
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isInBoundary(nr, nc) and mat[nr][nc] == 'O':
                    dfs(nr, nc)
        
        # Step 1: Mark all boundary-connected 'O'
        for r in range(n):
            for c in [0, m - 1]:  # First and last column
                if mat[r][c] == 'O':
                    dfs(r, c)
        for c in range(m):
            for r in [0, n - 1]:  # First and last row
                if mat[r][c] == 'O':
                    dfs(r, c)
                    
        # Step 2: Replace unmarked 'O' with 'X', 
        #and restore marked 'M' to 'O'
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'O':
                    mat[r][c] = 'X'  # Surrounded 'O' replaced with 'X'
                elif mat[r][c] == 'M':
                    mat[r][c] = 'O'  # Restore boundary-connected 'O'
    
        return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            s = list(map(str, input().split()))
            mat.append(s)

        ob = Solution()
        ans = ob.fill(mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends