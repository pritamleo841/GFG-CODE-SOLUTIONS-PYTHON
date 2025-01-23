#User function Template for python3
class Solution:
    def check(self, N, M, Edges): 
        #code here
        # Initialize the graph
        graph = {}
    
        def add_edge(u, v):
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
    
        # Add edges to the graph
        for u, v in Edges:
            add_edge(u, v)
    
        #Ensure that all nodes from 0 to N-1 are in the graph,
        #even if they have no edges
        for i in range(N):
            if i not in graph:
                graph[i] = []
    
        def dfs(node, visited, path_len):
            #If all nodes have been visited,
            #we've found a Hamiltonian path
            if path_len == N:
                return True
            
            # Explore all neighbors
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if dfs(neighbour, visited, path_len + 1):
                        return True
                    visited.remove(neighbour)  # Backtrack
            return False
    
        # Try starting the DFS from every node
        for node in range(N):
            visited = set()
            visited.add(node)
            if dfs(node, visited, 1):  # Start with node and path_len=1
                return True
        
        # If no Hamiltonian path is found
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends