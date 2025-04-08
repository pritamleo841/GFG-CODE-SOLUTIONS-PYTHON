#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        n=len(mat)
        visited = [[False for _ in range(n)] for _ in range(n)]
        ans = []
        
        if mat[0][0]==0 or mat[n-1][n-1]==0:
            return []
        #directions array
        directions=[('D',1,0),('L',0,-1),('R',0,1),('U',-1,0)]
        #check if safe to traverse to cell (r,c)
        def isSafe(r,c):
            return 0<=r<n and 0<=c<n and mat[r][c]==1 and not visited[r][c]
        #backtracking solution
        def backtrack(row,col,path):
            if (row,col)==(n-1,n-1):
                ans.append(path)
                return
            visited[row][col]=True #mark visited 
            for move,dr,dc in directions:
                nr,nc=row+dr,col+dc
                if isSafe(nr,nc):
                    backtrack(nr,nc,path+move)
            visited[row][col]=False #unmark visited
        
        backtrack(0,0,"")
        return ans
                    
        
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends