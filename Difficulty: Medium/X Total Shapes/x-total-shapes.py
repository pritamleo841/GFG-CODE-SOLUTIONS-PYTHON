
from collections import deque
class Solution:
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		#Code here
		#we will need to implement bfs algorithm here
		n,m = len(grid),len(grid[0])
		directions = [(0,-1),(1,0),(0,1),(-1,0)]
		queue=deque()
		visited = set()
		count=0
		
		def isInBoundary(r,c):
		    return 0<=r<n and 0<=c<m
		    
		for r in range(n):
		    for c in range(m):
		        #if at any point any unvisited X is encountered,
		        #increment the count by 1
		        if grid[r][c]=='X' and (r,c) not in visited:
		            queue.append((r,c))
                    visited.add((r,c))
                    count+=1
                    
                    while queue:
                        row,col = queue.popleft()
                        for dr,dc in directions:
                            nr,nc = row+dr,col+dc
                            if(
                                (nr,nc) not in visited
                                and isInBoundary(nr,nc)
                                and grid[nr][nc]=='X'
                            ):
                                queue.append((nr,nc))
                                visited.add((nr,nc))
                    
        return count

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = [['#' for i in range(m)] for j in range(n)]
        for i in range(n):
            s = input().strip()
            for j in range(m):
                grid[i][j] = s[j]
        obj = Solution()
        ans = obj.xShape(grid)
        print(ans)
        print("~")

# } Driver Code Ends