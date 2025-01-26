#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
import heapq
from typing import List, Tuple


# } Driver Code Ends

import heapq
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
       # Your code here
       #Priority queue for Dijkstra's algorithm
        pq = []  # Default min heap
        heapq.heappush(pq, (0, src))  # (distance, node)
        
        n = len(adj)  # Total number of vertices
        # Distance array to store shortest distances
        dist = [float('inf')] * n
        dist[src] = 0  # Distance to source is 0
        
        while pq:
            curr_dist, u = heapq.heappop(pq)  # Get the closest node
            
            # If the current distance is greater than the recorded distance, skip
            if curr_dist > dist[u]:
                continue
            
            # Traverse all neighbors of u
            for v, weight in adj[u]:
                # If there is a shorter path to v through u
                if curr_dist + weight < dist[v]:
                    dist[v] = curr_dist + weight
                    heapq.heappush(pq, (dist[v], v))  # Push updated distance to the heap
        
        return dist
        
        
        
        
        
        

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append((v, w))
            adj[v].append((u, w))
        src = int(input())
        ob = Solution()

        res = ob.dijkstra(adj, src)
        for i in res:
            print(i, end=" ")
        print()
        print("~")
# } Driver Code Ends