#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		#TC : O(V*E)
		#SC : O(V)
		#check for connected components
		for src in range(n):
    		#we will use bellman ford to detect negetive cycle
    		dist = [10**8]*n
    		dist[src]=0
    		
    		for _ in range(n-1):
    		    for u,v,wt in edges:
    		        if dist[u]!=10**8 and dist[u]+wt<dist[v]:
    		           dist[v]=dist[u]+wt
    		 
    		for u,v,wt in edges:
    		        if dist[u]!=10**8 and dist[u]+wt<dist[v]:
    		           return 1 #contains negetive weight cycle
		return 0 #doesn't contain negetive weight cycle
		


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.isNegativeWeightCycle(n, edges)
        print(ans)

        print("~")

# } Driver Code Ends