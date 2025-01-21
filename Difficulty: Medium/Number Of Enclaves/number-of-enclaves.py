#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        #The main task is to exclude all land cells (1s) 
        #that are connected to the boundary.
        
        n,m = len(grid),len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count=0
        
        def isOutOfBoundary(r,c):
            return 0<=r<n and 0<=c<m
            
        def dfs(r,c):
            if not isOutOfBoundary(r,c) or grid[r][c]==0:
                return
            grid[r][c]=0 #mark cell as visited
            for dr,dc in directions:
                newRow,newCol = r+dr,c+dc
                dfs(newRow,newCol)
        
        #remove land sides connected to the boundary
        for r in range(n):
            for c in [0,m-1]:  # Check first and last column
                if grid[r][c]==1:
                    dfs(r,c)
        
        for c in range(m):
            for r in [0,n-1]: # Check first and last row
                if grid[r][c]==1:
                    dfs(r,c)       
        
        #after removing everything from the boundary, 
        #now check how many 1s are there inside the grid      
        for r in range(n):
            for c in range(m):
                if grid[r][c]==1:
                    count+=1
                
        return count
                    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
        print("~")
# } Driver Code Ends