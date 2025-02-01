#User function Template for python3
from collections import deque
class Solution:
	def closedIslands(self,mat,N,M):
	    
		directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()

        def isInBoundary(r, c):
            return 0<=r<N and 0<=c<M

        def dfs(r,c):
            if not isInBoundary(r,c):
                return False
            if (r,c) in visited or mat[r][c] == 0:
                return True

            visited.add((r,c))
            is_closed = True
            for dr,dc in directions:
                if not dfs(r+dr,c+dc):  
                    is_closed = False
            return is_closed

        # Remove open islands
        for r in range(N):
            for c in [0,M-1]:
                if mat[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)
        for c in range(M):
            for r in [0,N-1]:
                if mat[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)

        # Count closed islands
        closed_islands = 0
        for r in range(1,N-1):
            for c in range(1,M-1):
                if mat[r][c]==1 and (r,c) not in visited:
                    if dfs(r,c):
                        closed_islands+=1

        return closed_islands


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
        print("~")
# } Driver Code Ends