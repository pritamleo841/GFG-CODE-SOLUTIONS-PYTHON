#User function Template for python3
from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        
        if A[0][0]==0:
            return -1
         # Directions for 4 possible moves (up, down, left, right)
        directions = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]
        
        # BFS Queue: stores (row, col, distance)
        queue = deque([(0, 0, 0)])  # Start from (0, 0) with 0 steps
        visited = set()
        visited.add((0, 0))
        
        # BFS Loop
        while queue:
            row, col, step = queue.popleft()
            
            # If the target is found, return the distance
            if (row, col) == (X, Y):
                return step
            
            # Explore the 4 possible directions
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # Check if the new position is within the grid and contains 1
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and A[nr][nc] == 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, step + 1))
        
        # Return -1 if the target is not reachable
        return -1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
        print("~")
# } Driver Code Ends