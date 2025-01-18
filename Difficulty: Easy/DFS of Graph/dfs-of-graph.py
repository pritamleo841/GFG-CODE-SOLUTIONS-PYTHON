#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        stack  = [];
        visited = [False]*len(adj)
        result = []
        
        #put into stack
        stack.append(0)
        
        while stack:
            current = stack.pop()
            #take element from stack, add to the result, mark as visited
            if not visited[current]:
                result.append(current)
                visited[current]=True
            #go to all neighbours of current adj list
            #if not visited already, add to stack,mark as visited
            
            #for left-to-right use reversed()
            for neighbour in reversed(adj[current]):
                if not visited[neighbour]:
                    stack.append(neighbour)
        return result


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")
# } Driver Code Ends