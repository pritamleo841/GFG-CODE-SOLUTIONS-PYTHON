#User function Template for python3
import math
class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
        '''
        Catalan Number(n) = Combination(2n,n)//(1+n)
        '''
        return math.comb(2*n,n)//(n+1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        ob = Solution()
        print(ob.numTrees(n))
        print("~")

# } Driver Code Ends