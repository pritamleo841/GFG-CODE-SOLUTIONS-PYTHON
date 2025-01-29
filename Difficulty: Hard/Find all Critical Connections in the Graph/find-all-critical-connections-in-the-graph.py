#User function Template for python3

class Solution:
    timer = 1 #stores the time to reach a node
    def criticalConnections(self, v, adj):
        #Find bridges using tarjan's algorithm
        # Reset timer for each function call
        self.timer = 1
        
        visited = [False] * v
        tin = [-1] * v  # Discovery time
        low = [-1] * v  # Earliest reachable ancestor
        bridges = []  # Store critical connections

        def dfs(node, parent):
            visited[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:  # Forward edge (tree edge)
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > tin[node]:  # Bridge condition
                        bridges.append((min(node, neighbor), max(node, neighbor)))
                else:  # Back edge case
                    low[node] = min(low[node], tin[neighbor])

        # Run DFS from each unvisited component
        for i in range(v):
            if not visited[i]:
                dfs(i, -1)

        return sorted(bridges)  # Return critical connections
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.criticalConnections(V, adj)
        for i in range(len(ans)):
            print(ans[i][0], ans[i][1])
        print("~")

# } Driver Code Ends