#User function Template for python3
from collections import deque
class Solution:
    def helpaterp(self, hospital):
        # code here
        #since a minimum time is needed, we will use BFS
        n,m = len(hospital),len(hospital[0])
        queue=deque()
        directions = [
            (0,-1),(1,0),(0,1),(-1,0)
        ]
        minTime = 0
        visited = set()
        
        def isInBoundary(r,c):
            return 0<=r<n and 0<=c<m
        #input all the infected patients into the queue
        for r in range(n):
            for c in range(m):
                if hospital[r][c]==2:
                    queue.append((r,c,0)) #u,v,time
                    visited.add((r,c))
        #bfs traversal
        while queue:
            r,c,time = queue.popleft()
            #store the maximum required time to infect all
            minTime = max(minTime,time)
            
            #go for 4 directions looking only for uninfected patients
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if(
                    (nr,nc) not in visited and
                    isInBoundary(nr,nc) and
                    hospital[nr][nc]==1 and hospital[nr][nc]!=0
                ):
                    queue.append((nr,nc,time+1))
                    visited.add((nr,nc))
        #If all patients are not infected after infinite units of time then simply return -1
        for r in range(n):
            for c in range(m):
                if hospital[r][c]==1 and (r,c) not in visited:
                    return -1
        return minTime
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        
        rc=input().split() #row and column
        r=int(rc[0])    
        c=int(rc[1])
        
        
        hospital=[]
        
        for i in range(r):
            hospital.append([int(j) for j in input().split()])
            
        ob = Solution()        
        print(ob.helpaterp(hospital))

        print("~")
# } Driver Code Ends