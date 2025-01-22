from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, mat):
		#Code here
		#we have rotten them simultaneouly, so BFS is needed not DFS
		n, m = len(mat), len(mat[0])  # Dimensions of the grid
        queue = deque()
        visited = set()  # To store visited (row, column)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
        maxTime = 0

        def isInBoundary(r, c):
            return 0 <= r < n and 0 <= c < m

        # Add all the rotten orange positions to the queue
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 2:
                    queue.append((r, c, 0))  # Initial time = 0
                    visited.add((r, c))

        # Start BFS traversal
        while queue:
            row, col, time = queue.popleft()
            maxTime = max(time, maxTime)  # Track the maximum time taken
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    isInBoundary(nr, nc)
                    and (nr, nc) not in visited
                    and mat[nr][nc] == 1  # Fresh orange
                ):
                    queue.append((nr, nc, time + 1))
                    visited.add((nr, nc))  # Mark as visited

        # Final check for any remaining fresh oranges
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1 and (r, c) not in visited:
                    return -1  # Fresh orange that couldn't be rotted

        return maxTime
#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends