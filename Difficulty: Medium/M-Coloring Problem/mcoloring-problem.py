# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        adjList=[[] for _ in range(v)]
        
        for u,w in edges:
            adjList[u].append(w)
            adjList[w].append(u)
        color=[0]*v #stores colors of each nodes
        
        #check if it is safe to color the current vertex
        def isSafe(node,currColor):
            for neighbor in adjList[node]:
                if color[neighbor]==currColor:
                    return False
            return True
        #backtracking solution
        def backtrack(node):
            if node==v:
                return True #All vertices are colored
            for c in range(1,m+1):
                if isSafe(node,c):
                    color[node]=c
                    if backtrack(node+1): #goto next color
                        return True
                    color[node]=0 #backtrack if not True
            return False
        
        return backtrack(0)
        


#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends