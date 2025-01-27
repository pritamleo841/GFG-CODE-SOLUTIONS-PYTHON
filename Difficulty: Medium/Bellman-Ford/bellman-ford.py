#User function Template for python3

class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        #code here
        #TC : O(V*E)
        #SC : O(V)
        #can detect if there is any negetive cycle
        dist = [10**8]*V
        dist[src]=0 #mark distance of source to source as 0
        
        for _ in range(V-1):#relaxation of edges to be done for (n-1) times
            for u,v,wt in edges:
                if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        
        #check for negetive cycle at nth time
        for u,v,wt in edges:
            if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                return [-1]
        return dist
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends