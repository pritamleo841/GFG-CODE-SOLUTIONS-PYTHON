
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
		n,m = len(grid),len(grid[0])
		directions = [(-1,0),(0,1),(1,0),(0,-1)]
		
		def isInBoundary(r,c):
		    return 0<=r<n and 0<=c<m
		
		def dfs(r,c):
		    if grid[r][c]==2:
		        return 1
		    grid[r][c] = -1  # Mark as visited
		    for dr,dc in directions:
		        nr,nc = r+dr,c+dc
		        if isInBoundary(nr,nc) and (grid[nr][nc]==3 or grid[nr][nc]==2):
		            if dfs(nr,nc):
		                return 1
		    return 0
		 
		for r in range(n):
		    for c in range(m):
		        if grid[r][c]==1:
		            return dfs(r,c)
		            
		return 0


#{ 
 # Driver Code Starts
T = int(input())
for i in range(T):
    n = int(input())
    grid = []
    for _ in range(n):
        a = list(map(int, input().split()))
        grid.append(a)
    obj = Solution()
    ans = obj.is_Possible(grid)
    if (ans):
        print("1")
    else:
        print("0")
    print("~")

# } Driver Code Ends