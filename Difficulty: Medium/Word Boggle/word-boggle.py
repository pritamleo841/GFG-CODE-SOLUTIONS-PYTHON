#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        n, m = len(board), len(board[0])  # Dimensions of the board
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
        ]
        ans = set()  # Use a set to avoid duplicate words
        
        def isInBoundary(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, node, visited, word):
            if node == "":
                ans.add(word)
                return
            
            # Mark the cell as visited
            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    isInBoundary(nr, nc) and
                    (nr, nc) not in visited and
                    board[nr][nc] == node[0]
                ):
                    dfs(nr, nc, node[1:], visited, word)
            
            # Backtrack: unmark the cell as visited
            #After exploring all directions, visited.remove((r, c)) 
            #restores the state, allowing the cell to be used in other paths.
            visited.remove((r, c))

        def isWordPresent(word):
            for r in range(n):
                for c in range(m):
                    if board[r][c] == word[0]:
                        dfs(r, c, word[1:], set(), word)

        # Check each word in the dictionary
        for word in dictionary:
            isWordPresent(word)

        return sorted(list(ans))  # Return sorted list of found words
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        dictionary = [x for x in input().strip().split()]
        line = input().strip().split()
        R = int(line[0])
        C = int(line[1])
        board = []
        for _ in range(R):
            board.append([x for x in input().strip().split()])
        obj = Solution()
        found = obj.wordBoggle(board, dictionary)
        if len(found) == 0:
            print(-1)
        else:
            found.sort()
            for i in found:
                print(i, end=' ')
            print()
        print("~")

# } Driver Code Ends