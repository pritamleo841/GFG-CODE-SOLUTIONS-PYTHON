#User function Template for python3
from collections import deque
class Solution:
    def shotestPath(self, mat, n, m, k):
        # Simple BFS using 3D visited array
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        queue = deque()
        # visited[row][col][remaining walls]
        #Possible values of remaining walls range from 0 to k, which means k+1 total states.
        #If we only allocate size k, the highest index (k) will be out of bounds.
        #To track all possibilities correctly, we need an extra index for k removals left.
        visited = [[[False]*(k+1) for _ in range(m)]for _ in range(n)]
        
        queue.append((0,0,0,k))
        visited[0][0][k]=True
        
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<m
        
        while queue:
            row,col,dist,walls = queue.popleft()
            if row==n-1 and col==m-1:
                return dist #if we reach the bottom corner
                
            for dr,dc in directions:
                nr,nc = row+dr,col+dc
                #check other neighbors
                if not isInBoundary(nr,nc):
                    continue
                #reduce wall count if it's a wall
                new_walls = walls - mat[nr][nc]
                
                if new_walls>=0 and not visited[nr][nc][new_walls]:
                    queue.append((nr,nc,dist+1,new_walls))
                    visited[nr][nc][new_walls]=True
                    
        return -1 #if not reachable
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m,k=map(int,input().split())
        mat=[]
        for i in range(n):
            row = list(map(int,input().split()))
            mat.append(row)
        
        ob = Solution()
        print(ob.shotestPath(mat,n,m,k))
        print("~")
# } Driver Code Ends