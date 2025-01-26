from collections import deque
class Solution:
	def isBipartite(self, adj):
		#code here
		n = len(adj)
		color = [-1]*n
		queue = deque()
		
		def checkBipartite(start,adj,color):
		    queue.append(start)
    		color[start] = 0 #use two colors - 0  and 1
    		
    		while queue:
    		    node = queue.popleft()
    		    #go through all the adjacent node
    		    for u in adj[node]:
    		        #if not colored, color it and add to queue
    		        if color[u]==-1:
    		            color[u]=1-color[node] #0->1 or 1->0 conversion
    		            queue.append(u)
    		        #if node and adjacent node has same color, not bipartite
    		        elif color[u]==color[node]:
    		            return False
    		return True
    	
    	for u in range(n):
    	    if color[u]==-1:
    	        if checkBipartite(u,adj,color)==False:
    	            return False
    	return True
    	        
    		
	
		
		
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)
               ]  # Fixed unnecessary use of `i` in list comprehension
        for _ in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(adj)
        if ans:  # Properly indented
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends