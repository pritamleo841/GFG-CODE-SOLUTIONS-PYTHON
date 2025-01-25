#User function Template for python3
from collections import deque
class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here
        #the trick here is to start from Y and find X; not vice versa
        #using bfs algorithm only. Go for cardinal directions only
        directions = [
            (-1,0),(0,1),(1,0),(0,-1)
        ]
        queue=deque()
        visited = set()
        
        def isInBoundary(r,c):
            return 0<=r<N and 0<=c<M
        
        for u in range(N):
            for v in range(M):
                if grid[u][v]=='Y':
                    queue.append((u,v,0))
                    visited.add((u,v))
        while queue:
            row,col,dist = queue.popleft()
            if grid[row][col]=='X':
                return dist
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                if(isInBoundary(nr,nc) and (nr,nc) not in visited):
                        queue.append((nr,nc,dist+1))
                        visited.add((nr,nc))
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        grid = []
        for i in range(N):
            ch = list(map(str,input().split()))
            grid.append(ch)
            
        ob = Solution()
        print(ob.shortestXYDist(grid,N,M))
        print("~")
# } Driver Code Ends