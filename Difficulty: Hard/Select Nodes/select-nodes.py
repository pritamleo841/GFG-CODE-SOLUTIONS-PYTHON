#User function Template for python3

class Solution:
    def countVertex(self, N, edges):
        #DFS solution
        adj = [[] for _ in range(N)]
        visited = [False]*N 
        count = 0
        for v,u in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        def dfs(root):
            nonlocal count
            visited[root]=True
            selected = False
            #Parent must be selected if the child isn't
            for neighbor in adj[root]:
                if not visited[neighbor] and not dfs(neighbor):
                    selected = True
            if selected:
                count+=1
            return selected
            
        dfs(0)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        edges=[]
        for _ in range(N-1):
            arr = list(map(int,input().split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(N, edges))
        print("~")
# } Driver Code Ends