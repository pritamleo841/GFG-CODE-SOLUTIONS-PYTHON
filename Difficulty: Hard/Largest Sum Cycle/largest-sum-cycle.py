#User function Template for python3
class Solution():
    def largestSumCycle(self, N, Edge):
        #DFS+Cycle Detection
        #TC - O(N), SC - O(N)
        visited = [False] * N  # To track visited nodes
        in_stack = [False] * N  # To track nodes in the current DFS path
        cycle_sums = {}  # To store sum of cycles

        def dfs(node, path):
            # Track the current path for cycle detection
            if in_stack[node]:
                # A cycle is detected
                cycle_index = path.index(node)  # Find the start of the cycle
                cycle_nodes = path[cycle_index:]  # Get the cycle nodes
                cycle_sum = sum(cycle_nodes)  # Sum of node indexes in the cycle
                return cycle_sum
            if visited[node]:
                return 0  # Already processed node, no cycle

            # Mark the node as visited and part of the current DFS path
            visited[node] = True
            in_stack[node] = True
            path.append(node)

            next_node = Edge[node]
            cycle_sum = 0
            if next_node != -1:
                cycle_sum = dfs(next_node, path)

            # Backtrack
            path.pop()
            in_stack[node] = False

            return cycle_sum

        max_cycle_sum = -1
        for i in range(N):
            if not visited[i]:
                cycle_sum = dfs(i, [])
                if cycle_sum > 0:
                    max_cycle_sum = max(max_cycle_sum, cycle_sum)

        return max_cycle_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge=[int(i) for i in input().split()]
        print(Solution().largestSumCycle(N, Edge))
        print("~")
# } Driver Code Ends