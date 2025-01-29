#User function Template for python3

class Solution():
    def maxWeightCell(self, Edge):
        n = len(exits)
        # Initialize weight array with zeros
        weight = [0]*n
    
        # Step 1: Calculate the weights
        for i in range(n):
            if exits[i] != -1:
                weight[exits[i]] += i
    
        # Step 2: Find the cell with maximum weight
        max_wt = float('-inf')
        max_index = 0
        for i in range(n):
            if weight[i] >= max_wt :
                max_wt = weight[i]
                max_index = i
    
        return max_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        exits = [int(i) for i in input().split()]
        sln = Solution()
        print(sln.maxWeightCell(exits))
        print("~")

# } Driver Code Ends