
from typing import List
class Solution:
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(0,1)]; #right and down only
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<m
        paths = []
        def recur(r,c,path):
            new_path=path+[grid[r][c]] #new path,instead of using append()
            if r==n-1 and c==m-1:
                paths.append(new_path)
                return
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if isInBoundary(nr,nc):
                    recur(nr,nc,new_path)
        recur(0,0,[])
        return paths
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        grid=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findAllPossiblePaths(a[0],a[1], grid)
        
        IntMatrix().Print(res)
        

        print("~")
# } Driver Code Ends