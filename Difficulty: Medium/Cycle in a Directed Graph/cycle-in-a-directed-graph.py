#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        #using kahn's algorithm concept
        queue=deque()
        indegree=[0]*V
        count=0
        
        for u in range(V):
            for neighbor in adj[u]:
                indegree[neighbor]+=1
        
        #push all the vertices with indegree=0
        for v in range(V):
            if indegree[v]==0:
                queue.append(v)
        
        while queue:
            node = queue.popleft()
            count+=1
            
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        #if nodes processed is not equal to number of vertices
        #there is a cycle, otherwise not
        return count!=V 
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
        print("~")
# } Driver Code Ends