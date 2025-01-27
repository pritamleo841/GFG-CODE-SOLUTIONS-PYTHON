#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		#convert -1 to infinity/or large value for sake of easier computation
		n = len(matrix)
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j]==-1:
		            matrix[i][j]=float('inf')
		        if i==j: #all diagonal elements(vertex to itself) is 0
		            matrix[i][j]=0
		 
		 #precomputation for n edges
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
		'''
		 to check for negetive cycles - 
		 for i in range(n):
		    if matrix[i][i]<0:
		        print('Contains negetive cycle')
		'''
		 
		 #revert back the values from infinity to 0
		 #for unreachable edges
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j]==float('inf'):
		             matrix[i][j]=-1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.shortest_distance(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends