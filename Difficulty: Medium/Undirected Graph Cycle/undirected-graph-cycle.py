from typing import List
class DisjointSet:
    def __init__(self,n):
        self.rank = [0]*n
        self.parent = list(range(n))
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u!=parent_v:
            if self.rank[parent_u]<self.rank[parent_v]:
                self.parent[parent_u] = parent_v
            elif self.rank[parent_v]<self.rank[parent_u]:
                self.parent[parent_v] = parent_u
            else:
                self.parent[parent_v] = parent_u
                self.rank[parent_u]+=1
                
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		ds = DisjointSet(V)
		for u in range(V):
		    for v in adj[u]:
		        if u < v:  # Avoid duplicate edges
    		        if ds.find(u)==ds.find(v): #if both have same parents
    		            return 1
		            ds.union(u,v) #union them
		return 0
		 


#{ 
 # Driver Code Starts
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
        print("~")

# } Driver Code Ends