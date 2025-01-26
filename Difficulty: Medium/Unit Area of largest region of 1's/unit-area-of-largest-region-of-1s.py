

class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		#Code here
		n,m=len(grid),len(grid[0])
		maxArea = 0
		directions = [
		    (-1,0),(0,1),(1,0),(0,-1),
		    (-1,-1),(-1,1),(1,-1),(1,1)
		]
		
		def isInBoundary(r,c):
		    return 0<=r<n and 0<=c<m
		    
		def dfs(r,c):
		    #if grid[r][c] is out of boundary or 0, no need to check futher
		    if not isInBoundary(r,c) or grid[r][c]==0:
		        return 0
		    grid[r][c]=0 #mark it as 0(visited),to avoid cycle
		    area=1
		    #go to 8 directions
		    for dr,dc in directions:
		        nr,nc = r+dr,c+dc
		        area+=dfs(nr,nc) #calculate area of each direction
		 
		    return area
		#check for every connected component
		for r in range(n):
		    for c in range(m):
		        if grid[r][c]==1:
		            #from any 1,check all its neightbouring 1
		            area = dfs(r,c)
		            #save max area of each connected component visited
		            maxArea=max(area,maxArea)
		return maxArea



#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

        print("~")
# } Driver Code Ends