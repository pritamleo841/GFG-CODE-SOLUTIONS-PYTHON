import heapq
class Solution:
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
	    #Dijkstra's algorithm to find minimum cost path
	    #TC - O(N^2 * log(N)) for N^2 cells processing
	    #SC - Cost array - O(N^2)
	    directions = [(0,-1),(0,1),(1,0),(-1,0)]
	    n=len(grid)
	    pq = []
	    #starting from the top-left corner
	    heapq.heappush(pq,(0,0,grid[0][0])) #row,col,cost
	    #cost array with maximum values
	    costs = [[float('inf')]*n for _ in range(n)]
	    costs[0][0]=grid[0][0] #helps in edge relaxation
	    
	    def isInBoundary(r,c):
	        return 0<=r<n and 0<=c<n
	        
	    while pq:
	        row,col,cost = heapq.heappop(pq)
	        #return cost,if we reach the bottom-left corner
	        if row==n-1 and col==n-1:
	            return costs[row][col] #return cost
	        for dr,dc in directions:
	            nr,nc = row+dr,col+dc
	            if isInBoundary(nr,nc):
	                newCost = cost+grid[nr][nc]
	                #Only update if we found a cheaper path to the neighbor
	                if newCost<costs[nr][nc]: #relaxation of edge (nr,nc)
	                    costs[nr][nc]=newCost
	                    heapq.heappush(pq,(nr,nc,newCost))
	    return -1
		          
		 


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends