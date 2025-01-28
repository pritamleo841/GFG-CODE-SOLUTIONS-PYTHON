#User function Template for python3
from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        #simple bfs to count all the unvisited 1s
        n,m=len(grid),len(grid[0])
        queue=deque()
        #all the 8 directions are to be considered
        directions = [
            (0,-1),(1,0),(0,1),(-1,0),
            (-1,-1),(1,-1),(-1,1),(1,1)
        ]
        visited=set()
        island=0
        
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<m
        
        def bfs(start_row,start_col):
            queue.append((start_row,start_col))
            visited.add((start_row,start_col))
            
            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if(
                        (nr,nc) not in visited
                        and isInBoundary(nr,nc)
                        and grid[nr][nc]==1
                    ):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        
        for r in range(n):
            for c in range(m):
                #count each disconnected 1s, i.e., new islands
                if grid[r][c]==1 and (r,c) not in visited:
                    island+=1
                    bfs(r,c)
        return island


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends