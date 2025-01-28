from collections import deque
class Solution:
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        
        #Kahn's Algorithm
        #TC - O(V+E), SC - O(V)
        n=len(adj)
        indegree = [0]*n
        queue=deque()
        topo = []
        #store all the indegrees in a list
        for v in range(n):
            for neighbor in adj[v]:
                indegree[neighbor]+=1
        #push all the vertices with indegree=0
        for v in range(n):
            if indegree[v]==0:
                queue.append(v)
        #do a bfs traversal
        while queue:
            node = queue.popleft()
            #add node to resultant list 
            topo.append(node)
            #reduce indegree for each adjacent node by 1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                #if indegree is 0, append to the queue
                if indegree[neighbor]==0:
                    queue.append(neighbor)
                    
        return topo
        
        '''
        #Using dfs to get topological sorted list
        #TC - O(V+E), SC - O(V)
        n=len(adj)
        stack = [] #use stack to store visited nodes
        topo = []
        visited = [False]*n
        
        #simple dfs logic
        def dfs(v):
            visited[v]=True #mark as visited
            for neighbor in adj[v]: #check for each neighbor
                if not visited[neighbor]: #if not visited , dfs it
                    dfs(neighbor)
            #after everything , append node to stack
            stack.append(v)
        
        for v in range(n): #check for each node 
            if not visited[v]: #if not visited,dfs it
                dfs(v)
        while stack: #pop each element from stack and add to resultant list
            topo.append(stack.pop())
        return topo
        
        '''
        
        
        



#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        e = int(input())
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topologicalSort(adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
        print("~")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends