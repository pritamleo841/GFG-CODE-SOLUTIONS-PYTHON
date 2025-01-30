#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        #SC - O(V)
        visited = [0] * V  # 0 = unvisited, 1 = visiting, 2 = safe
        #TC - O(V+E)
        def isSafe(node):
            if visited[node] > 0:  
                return visited[node] == 2  # Return True if safe, False if in cycle
            
            visited[node] = 1  # Mark as visiting
            for neighbor in adj[node]:
                if visited[neighbor] == 2:  # If already safe, skip DFS
                    continue
                if visited[neighbor] == 1 or not isSafe(neighbor):  # Found a cycle
                    return False
            
            visited[node] = 2  # Mark as safe
            return True
        
        # Collect safe nodes
        return sorted([node for node in range(V) if isSafe(node)])
        '''
        #using topological sort
        adjR = [[] for _ in range(V)] #SC - O(V*V)
        indegree = [0]*V #stores indegree
        #get a reversed adjacency list, u->v becomes v->u
        for u in range(V):
            for v in adj[u]:
                adjR[v].append(u)
                indegree[u]+=1
        
        queue = deque()
        safeNodes = [] #store the safenodes(i.e., indegree=0 nodes)
        #do a topological sort #TC - O(V+E)
        for v in range(V):
            if indegree[v]==0:
                queue.append(v)
       
        while queue:
            node = queue.popleft()
            safeNodes.append(node) #stores the safenodes with indegree=0
            for v in adjR[node]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        
        return sorted(safeNodes) #TC - O(VLOGV)
        '''



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


        print("~")
# } Driver Code Ends