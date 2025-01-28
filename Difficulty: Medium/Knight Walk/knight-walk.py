from collections import deque
class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
		queue=deque()
		visited=set()
		#Directions for Knight's movement: 8 possible moves(L moves only)
		#2 steps in one direction and 1 step in a perpendicular direction.
        directions = [
            (-2,-1),(-2,1),(-1,-2),(-1,2),
            (1,-2),(1,2),(2,-1),(2,1)
        ]
		
		def isInBoundary(r,c):
		    return 1<=r<=N and 1<=c<=N
		'''
		BFS is the most suitable algorithm to find the minimum number of steps for this problem 
		because it ensures that the shortest path is found by exploring all positions level by level.
		'''
		queue.append((KnightPos[0],KnightPos[1],0))
		visited.add((KnightPos[0],KnightPos[1]))
		
		while queue:
		    row,col,step = queue.popleft()
		    if row==TargetPos[0] and col==TargetPos[1]:
		       return step
		        
		    for dr,dc in directions:
		        nr,nc=row+dr,col+dc
		        if isInBoundary(nr,nc) and (nr,nc) not in visited:
		                queue.append((nr,nc,step+1))
		                visited.add((nr,nc))
		return -1


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends