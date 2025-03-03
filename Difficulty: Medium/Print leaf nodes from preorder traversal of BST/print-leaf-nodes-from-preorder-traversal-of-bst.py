#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		stack = [] 
        leaves = []
        # Iterate through the preorder list
        for i in range(N-1):
            found = False
            # Push current node if it's greater than the next node
            if arr[i]>arr[i+1]:
                stack.append(arr[i])
            else:
                # Pop elements from stack until current node is 
                # less than or equal to top of stack
                while stack and arr[i+1]>stack[-1]:
                    stack.pop()
                    found = True
            # If a leaf node is found, add it to the leaves list
            if found:
                leaves.append(arr[i])
        # Since the rightmost element is always a leaf node
        leaves.append(arr[-1])
        return leaves



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        print("~")
# } Driver Code Ends