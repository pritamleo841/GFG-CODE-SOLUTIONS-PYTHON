#User function Template for python3

class Solution:
    
    #Function to return a list of lists of integers denoting the members 
    #of strongly connected components in the given graph.
    def __init__(self):
        self.time = 0  # Global counter for DFS discovery time

    def tarjans(self, V, adj):
        # Initialization
        self.disc = [-1] * V  # Discovery times
        self.low = [-1] * V  # Lowest discovery time reachable
        self.stack = []  # Stack for Tarjan's algorithm
        self.in_stack = [False] * V  # Track nodes in stack
        self.SCCs = []  # List of SCCs

        # Helper DFS function
        def dfs(u):
            self.disc[u] = self.low[u] = self.time
            self.time += 1
            self.stack.append(u)
            self.in_stack[u] = True

            # Explore all adjacent vertices
            for v in adj[u]:
                if self.disc[v] == -1:  # If not visited, recurse
                    dfs(v)
                    self.low[u] = min(self.low[u], self.low[v])
                elif self.in_stack[v]:  # If in stack, it's a back edge
                    self.low[u] = min(self.low[u], self.disc[v])

            # If u is the root of an SCC, pop stack to extract SCC
            if self.low[u] == self.disc[u]:
                scc = []
                while True:
                    node = self.stack.pop()
                    self.in_stack[node] = False
                    scc.append(node)
                    if node == u:
                        break
                self.SCCs.append(sorted(scc))  # Store SCC (sorted for consistency)

        # Call DFS for every unvisited node
        for i in range(V):
            if self.disc[i] == -1:
                dfs(i)

        return sorted(self.SCCs)  # Sort SCCs lexicographically


#{ 
 # Driver Code Starts
#Initial Template for Python 3
from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        ob = Solution()
        
        ptr = ob.tarjans(V, adj)
        
        for i in range(len(ptr)):
            for j in range(len(ptr[i])):
                if j==len(ptr[i])-1:
                    print(ptr[i][j],end="")
                else:
                    print(ptr[i][j],end=" ")
            print(",",end="")
        print()
        print("~")
# } Driver Code Ends