class Solution:
	def isWordExist(self, board, word):
		#Code here
		n,m = len(board),len(board[0])
		directions = [
		    (-1,0),(0,1),(1,0),(0,-1) #up,down,left,right
		]
		
		def isInBoundary(r,c):
		    return 0<=r<n and 0<=c<m
		
		def dfs(r,c,node,visited):
		    #base condition
		    if not node:
		        return True
		        
		    visited.add((r,c)) #visited
		    
		    for dr,dc in directions:
		        nr,nc = r+dr,c+dc
		        if (
		            isInBoundary(nr,nc) 
		            and (nr,nc) not in visited 
		            and board[nr][nc]==node[0]):
		                #if whole node is explored, return True
		                if dfs(nr,nc,node[1:],visited):
		                    return True
		                
		    visited.remove((r,c)) #backtrack
		    return False
		    
		for r in range(n):
		     for c in range(m):
		         if board[r][c]==word[0]:
		             if dfs(r,c,word[1:],set()): #if present, then return true
		                 return True
		#defualt return False
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            board.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(board, word)
        if (ans):
            print("1")
        else:
            print("0")
        print("~")
# } Driver Code Ends