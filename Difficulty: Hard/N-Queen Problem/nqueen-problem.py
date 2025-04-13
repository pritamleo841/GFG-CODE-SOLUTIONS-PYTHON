#User function Template for python3

class Solution:
    def nQueen(self, n):
        '''
        Diagonal ↘ (Top-left to Bottom-right): Formula: row - col
        ✅ Cells on this diagonal share the same row - col value.
        Example:
            (0, 0), (1, 1), (2, 2) → row - col = 0
            (1, 0), (2, 1), (3, 2) → row - col = 1
            
        🔹 Anti-diagonal ↙ (Top-right to Bottom-left): Formula: row + col
        ✅ Cells on this diagonal share the same row + col value.
        Example:
            (0, 3), (1, 2), (2, 1), (3, 0) → row + col = 3
        '''
        def backtrack(col,path):
            if col==n:
                ans.append([x+1 for x in path])
                return
            for row in range(n):
                if row in rows or (row-col) in diagonal or (row+col) in anti_diagonal:
                    continue
                #place queen
                path.append(row)
                rows.add(row)
                diagonal.add(row-col)
                anti_diagonal.add(row+col)
                backtrack(col+1,path)
                #backtrack
                path.pop()
                rows.remove(row)
                diagonal.remove(row-col)
                anti_diagonal.remove(row+col)
                
        ans = []
        rows = set()
        diagonal = set()
        anti_diagonal = set()
        backtrack(0,[])
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends