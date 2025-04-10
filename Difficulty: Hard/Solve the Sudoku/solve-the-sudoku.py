#User function Template for python3

class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        #Fill the sets and track empty cells
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num!=0:
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3+(j//3)].add(num)
                else:
                    empties.append((i,j))

        def backtrack(index):
            if index==len(empties):
                return True

            i,j=empties[index]
            box_idx = (i//3)*3+(j//3)

            for num in range(1,10):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    board[i][j]=num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(index+1):
                        return True

                    # Backtrack
                    board[i][j]=0
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)

            return False
            
        backtrack(0)
    '''
    #Function to find a solved Sudoku.  
    (TLE) ->
    def isValid(self,row,col,k,mat):
        for i in range(9):
            if mat[row][i]==k:
                return False
            if mat[i][col]==k:
                return False
            if mat[3*(row//3)+i//3][3*(col//3)+i%3]==k:
                return False
        return True
        
    def solve(self,mat):
        for i in range(9):
            for j in range(9):
                if mat[i][j]==0:
                    for k in range(1,10):
                        if self.isValid(i,j,k,mat):
                            mat[i][j]=k
                            if self.solve(mat):
                                return True
                            else:
                                mat[i][j]=0 #backtrack if false
                    return False
        return True #if solvable return true
        
    def solveSudoku(self, mat):
        self.solve(mat)
    '''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends