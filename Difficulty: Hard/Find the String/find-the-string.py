#User function Template for python3
'''
1.Use Hierholzer’s Algorithm (Eulerian Path/Circuit)

2.Construct a directed De Bruijn graph, where each node represents an (N-1)-length sequence.
Each edge corresponds to adding a character from {0, 1, ..., K-1}.
Find an Eulerian Path

3.Perform Hierholzer's Algorithm to find the Eulerian path in the De Bruijn graph.
Convert the path into a sequence

4.Start with the first N-1 characters.
Append only the last character from each transition.
'''
class Solution:
    def findString(self, N, K):
        # Use Hierholzer's algorithm to find an Eulerian path
        def dfs(node):
            for i in range(K):
                edge = node + str(i)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    result.append(str(i))
        
        # Start from the smallest lexicographic string "00..0"
        start = "0" * (N - 1)
        visited = set()
        result = []
        
        # Perform DFS to construct the Eulerian path
        dfs(start)
        
        # Construct the answer from the Eulerian path
        return start + "".join(result[::-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
        print("~")
# } Driver Code Ends