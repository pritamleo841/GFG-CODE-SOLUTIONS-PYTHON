#Back-end complete function Template for Python 3

class Solution:
    
    #Function to calculate the sum of dependencies for all vertices.
    def sumOfDependencies(self,V,edges):
        # code here
        
        #Idea is to check adjacency list 
        #and find how many edges are there from each vertex 
        #and return the total number of edges. 
        
        adjList = [[] for i in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            
        num = 0
        for u in range(V):
            num+=len(adjList[u])
        return num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())  # Number of test cases
    for _ in range(t):
        N = int(input())  # Number of nodes
        M = int(input())  # Number of edges

        edges = []
        for _ in range(M):
            x, y = map(int, input().split())  # Read the edge (u, v)
            edges.append([x, y])

        ob = Solution()
        print(ob.sumOfDependencies(N, edges))
        print("~")

# } Driver Code Ends