#User function Template for python3

class Solution:
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        #Using Tarjan's Algorithm
        self.timer = 0
        tin = [-1] * V  # Discovery time
        low = [-1] * V  # Lowest reachable ancestor
        visited = [False] * V
        bridges = set()  # Use a set for quick lookup

        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue  # Ignore the edge that leads to the parent

                if not visited[neighbor]:  # If unvisited, perform DFS
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    # **Bridge condition**
                    if low[neighbor] > tin[node]:  
                        bridges.add((min(node, neighbor), max(node, neighbor)))  # Store bridge in sorted order
                else:
                    # **Back edge case: Update low[node]**
                    low[node] = min(low[node], tin[neighbor])

        # **Run DFS for every disconnected component**
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        # **Check if (c, d) is a bridge**
        return 1 if (min(c, d), max(c, d)) in bridges else 0


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
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
        print("~")
# } Driver Code Ends