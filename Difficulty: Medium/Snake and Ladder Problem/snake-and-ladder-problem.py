# User function Template for Python3
from collections import deque
class Solution:
    def minThrow(self, N, arr):
        # code here
        board = list(range(30)) #5*6 size snake and ladder board
        #arr[] of 2*N size where 2*i and (2*i + 1)th values denote 
        #the starting and ending point respectively of ith snake or ladder.
        for i in range(0,2*N,2):
            start,end = arr[i]-1,arr[i+1]-1 #converting to 0-based indexing
            board[start]=end
        #Input N = 8, Arr = [3 22 5 8 11 26 20 29 17 4 19 7 27 1 21 9]
        #Board(0-based) = [0, 1, 21, 3, 7, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 3, 17, 6, 28, 8, 21, 22, 23, 24, 25, 0, 27, 28, 29]
        queue=deque()
        visited = [False]*30
        queue.append((0,0)) #current cell , dice throws
        visited[0]=True #first cell visited
       
        while queue:
            currentCell,diceThrows=queue.popleft()
            if currentCell == 29:
                return diceThrows
            for diceRoll in range(1,7): #exploring next 7 consecutive positions
                nextCell = currentCell + diceRoll
                if nextCell<30 and not visited[nextCell]:
                    # Move to the position considering snake or ladder
                    actualCell = board[nextCell] #need to go to the actual cell
                    queue.append((actualCell, diceThrows + 1))
                    visited[nextCell] = True
        return -1
                
            
        

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
        print("~")
# } Driver Code Ends