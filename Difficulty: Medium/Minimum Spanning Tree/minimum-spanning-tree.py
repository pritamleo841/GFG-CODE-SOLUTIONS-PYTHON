# User function Template for python3
from typing import List
'''
TC : 1. Sorting- O(ElogE) and UnionFind - O(E*4alpha).Total - O(ElogE)
SC : O(V+E)
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Correct initialization
        self.rank = [0] * n  # Rank initialized to 0 for all vertices

    def findUParent(self, u: int) -> int:
        # Path compression
        if u != self.parent[u]:
            self.parent[u] = self.findUParent(self.parent[u])
        return self.parent[u]

    def unionByRank(self, u: int, v: int):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        if ulp_u == ulp_v:
            return
        # Union by rank
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

class Solution:
    # Function to find the sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[List[int]]]) -> int:
        edges = []
        # Construct edge list from adjacency list
        for u in range(V):
            for neighbour, weight in adj[u]:
                if u < neighbour:  # Avoid duplicate edges (undirected graph)
                    edges.append((weight, u, neighbour))
        
        # Sort edges by weight
        edges.sort()

        # Initialize Union-Find structure
        uf = UnionFind(V)
        mstWt = 0

        # Process edges in sorted order
        for wt, u, v in edges:
            if uf.findUParent(u) != uf.findUParent(v):
                uf.unionByRank(u, v) #connect the edges
                mstWt += wt  # Include edge in MST

        return mstWt
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
        print("~")

# } Driver Code Ends