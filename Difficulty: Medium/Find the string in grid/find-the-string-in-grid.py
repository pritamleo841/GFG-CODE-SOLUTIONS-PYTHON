#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		#check for boundary values
		def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m
        #search in a particular direction
        def search_direction(x, y, dx, dy):
            for k in range(len(word)):
                nx, ny = x + k * dx, y + k * dy
                if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                    return False
            return True
        #from (i,j) search in all 8 directions
        def search_from_cell(x, y):
            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # up, down, left, right
                (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
            ]
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    return True
            return False
        
        n, m = len(grid), len(grid[0])
        result = []
        #check for each cell
        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0] and search_from_cell(i, j):
                    result.append((i, j))
    
        #result.sort()  # Ensure lexicographical order
        return result
		                           


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        grid = []
        for _ in range(n):
            cur = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end=" ")
            print()
        if len(ans) == 0:
            print(-1)

        print("~")

# } Driver Code Ends