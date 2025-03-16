#User function Template for python3

class Solution:
    def canRepresentBST(self, arr, N):
        #Using monotonic stack here
        '''
        1.Every new node in the array follows BST properties.
        2. If a node is greater than the last popped value, 
            it must be in the right subtree of some ancestor.
        '''
        stack = []
        root = float('-inf')
        for i in range(N):
            #No current value can be less than the root value
            if arr[i]<root:
                return 0
            #Pop elements from stack while they are smaller than the current value
            while stack and arr[i]>stack[-1]:
                root = stack.pop()
            stack.append(arr[i])
        #If entire array is processed,it is a valid preorder
        return 1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
        print("~")
# } Driver Code Ends