#User function Template for python3
from collections import deque
from typing import List
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        queue  = deque();
        visited = [False]*len(adj)
        result = []
        
        #put into queue, mark as visited then
        queue.append(0)
        visited[0]=True
        
        while queue:
            current = queue.popleft()
            result.append(current)
            #go to all neighbours of current adj list
            #if not visited already, add to queue,mark as visited
            for neighbour in adj[current]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour]=True
        return result
            
    

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends