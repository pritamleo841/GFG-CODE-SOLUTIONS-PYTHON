#User function Template for python3
from collections import deque
class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        '''
        1.The worst-case scenario for filling the matrix occurs when the farthest cell from (X, Y) is filled last.
        2.The maximum distance from (X, Y) to any corner (or edge) determines the minimum required iterations.
        3.We compute the maximum Manhattan Distance from (X, Y) to the four corners of the matrix:

        maxSteps=max(X−1,N−X)+max(Y−1,M−Y)
        X-1: Distance to the topmost row
        N-X: Distance to the bottommost row
        Y-1: Distance to the leftmost column
        M-Y: Distance to the rightmost column

        '''
        # Calculate maximum Manhattan distance to any matrix boundary
        return max(x-1, N-x) + max(y-1, M-y)
        '''
        # Directions for BFS: Left, Right, Down, Up
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        # Convert 1-based indexing to 0-based
        x, y = x - 1, y - 1

        # BFS queue with multiple sources (all cells filled from (x, y))
        queue = deque([(x, y, 0)])  # (row, col, steps)
        
        # Visited matrix
        visited = [[False] * M for _ in range(N)]
        visited[x][y] = True  

        max_steps = 0  # Track the maximum distance

        while queue:
            row, col, step = queue.popleft()
            max_steps = step  # This ensures we store the last (max) step

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, step + 1))

        return max_steps
        '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        x, y = map(int, input().split())
        ob = Solution()
        print(ob.minIteration(N, M, x, y))
        print("~")

# } Driver Code Ends