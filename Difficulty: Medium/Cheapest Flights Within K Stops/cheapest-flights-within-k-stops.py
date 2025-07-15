#User function Template for python3
from typing import List
import heapq
from collections import defaultdict

class Solution:

    def CheapestFLight(self, n, flights, src, dst, k):
        '''
        Build the graph as an adjacency list.
        Use a priority queue with elements of the form (cost_so_far, current_node, stops_so_far).
        At each step, if current_node == dst, return cost_so_far.
        If stops_so_far <= k, push all neighbors into the queue with updated cost and stops.
        If the queue is empty and we never reached dst, return -1.
        '''
        
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        # Min-heap (cost, node, stops)
        heap = [(0, src, 0)]
        
        # best[node][stops] = minimum cost to reach node with stops
        best = dict()
    
        while heap:
            cost, node, stops = heapq.heappop(heap)
    
            # If destination is reached
            if node == dst:
                return cost
            
            # If we already visited this node with fewer or equal stops and less cost, skip
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            best[(node, stops)] = cost
            
            # Only continue if stops <= k
            if stops <= k:
                for nei, price in graph[node]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))
    
        return -1