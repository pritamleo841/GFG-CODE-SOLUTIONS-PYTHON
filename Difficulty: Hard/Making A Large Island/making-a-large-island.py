from typing import List
class DisjointSet :
    def __init__(self,n):
        self.size = [1]*(n*n)  # Store size of each component
        self.parent = list(range(n*n))  # Initially, each cell is its own parent

    def find(self,node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def unionBySize(self, u, v):
        uulp = self.find(u)  # Find ultimate parent of u
        vulp = self.find(v)  # Find ultimate parent of v
        
        if uulp != vulp:  # Merge only if they are in different sets
            if self.size[uulp] < self.size[vulp]:  
                self.parent[uulp] = vulp
                self.size[vulp] += self.size[uulp]
            else:
                self.parent[vulp] = uulp
                self.size[uulp] += self.size[vulp]

                
class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n)
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        
        def isInBoundary(r, c):
            return 0<=r<n and 0<=c<n
        
        # Merge connected 1s using DSU
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    nodeNo = r*n+c
                    for dr, dc in directions:
                        nr,nc = r+dr,c+dc
                        if isInBoundary(nr,nc) and grid[nr][nc] == 1:
                            adjNodeNo = nr*n+nc
                            ds.unionBySize(nodeNo, adjNodeNo)

        # Try flipping a single 0 to 1 and find max island
        maxSize = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # Only try flipping 0s
                    components = set()
                    for dr,dc in directions:
                        nr,nc=r+dr,c+dc
                        if isInBoundary(nr,nc) and grid[nr][nc] == 1:
                            components.add(ds.find(nr*n+nc))  # Add unique parents
                    
                    # Compute the total size
                    sizeTotal = 1  # +1 for the flipped cell
                    for component in components:
                        sizeTotal+=ds.size[component]
                    
                    maxSize = max(maxSize,sizeTotal)

        # Handle edge case where the grid is already filled with 1s
        for cellNo in range(n*n):
            maxSize = max(maxSize, ds.size[ds.find(cellNo)])

        return maxSize

#{ 
 # Driver Code Starts

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
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
        print("~")
# } Driver Code Ends