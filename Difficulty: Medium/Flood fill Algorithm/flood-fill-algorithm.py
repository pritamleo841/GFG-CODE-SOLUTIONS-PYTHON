class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		initialColor = image[sr][sc]
		flooded = [row[:] for row in image]
		if initialColor==newColor:
		    return flooded
		#checking for right,left,up,down
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		n,m=len(image),len(image[0])
		
		def isBoundaryValid(r,c):
		    return 0<=r<n and 0<=c<m
		    
		def isFloodFillValid(r,c):
		    return flooded[r][c]==initialColor and image[r][c]!=newColor
		    
		def dfs(r,c):
		    flooded[r][c] = newColor
		    for dr,dc in directions:
		        newRow,newCol = r+dr,c+dc
		        if isBoundaryValid(newRow,newCol) and isFloodFillValid(newRow,newCol):
		                dfs(newRow,newCol)
		
		dfs(sr,sc)
		return flooded
		



#{ 
 # Driver Code Starts
T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    # Print the modified image
    for row in ans:
        print(" ".join(map(str, row)))

    # Print the separator
    print("~")

# } Driver Code Ends