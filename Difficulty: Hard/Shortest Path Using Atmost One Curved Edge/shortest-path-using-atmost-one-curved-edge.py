#User function Template for python3
import heapq
class Solution:
    def shortestPath(self, n, m, a, b, edges):
        #Build the graph (only straight edges)
        graph = {i:[] for i in range(1,n+1)}
        curved_edges = []
        
        for u,v,w1,w2 in edges:
            graph[u].append((v,w1))
            graph[v].append((u,w1))
            curved_edges.append((u,v,w2)) #store curved edges separately
        
        #Dijsktra to find shortest path using straight edges
        def dijkstra(start):
            pq = [(0,start)] #min heap (dist,node)
            dist = {i:float('inf') for i in range(1,n+1)}
            dist[start]=0
            while pq:
                cost,node = heapq.heappop(pq)
                if cost>dist[node]:
                    continue
                for neighbor,wt in graph[node]:
                    newCost = cost + wt
                    if newCost < dist[neighbor]:
                        dist[neighbor] = newCost
                        heapq.heappush(pq,(dist[neighbor],neighbor))
            return dist
        #Compute shortest distances from a and from b using only straight edges
        distA = dijkstra(a)
        distB = dijkstra(b)
        #Compute the shortest path using at most one curved edge
        min_dist = distA[b] #Default: shortest path using only straight edges
        
        for u,v,wt in curved_edges:
            if distA[u]!=float('inf') and distB[v]!=float('inf'):
                min_dist=min(min_dist,distA[u]+wt+distB[v])
            if distA[v]!=float('inf') and distB[u]!=float('inf'):
                min_dist=min(min_dist,distA[v]+wt+distB[u])
                
        return -1 if min_dist==float('inf') else min_dist
        
        
                
                    
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**6) 
from heapq import *

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        a,b=map(int,input().split())
        edges = []
        for i in range(m):
            edge = list(map(int,input().split()))
            edges.append(edge)
        
        ob = Solution()
        print(ob.shortestPath(n,m,a,b,edges))
        print("~")
# } Driver Code Ends