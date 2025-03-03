class Solution:
    def buildTree(self, in_order, post_order):
        #O(n) solution
        inorderIdx = { v:i for i,v in enumerate(in_order)}
        
        def helper(l,r):
            if l>r:
                return None
            root = Node(post_order.pop())
            idx = inorderIdx[root.data]
            
            root.right = helper(idx+1,r)
            root.left = helper(l,idx-1)
            return root
            
        return helper(0,len(in_order)-1)
        
        '''
        O(n^2) solution-
        
        if not in_order:
            return None
        root = Node(post_order.pop())
        idx = in_order.index(root.data)
        root.right = self.buildTree(in_order[idx+1:],post_order)
        root.left = self.buildTree(in_order[:idx],post_order)
        return root
        '''
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

#Contributed by : PranchalK

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Helper function that allocates
# a new node
class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# This funtcion is here just to test
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        in_order = list(map(
            int,
            input().strip().split()))  # parent child info in list
        post_order = list(map(
            int,
            input().strip().split()))  # parent child info in list
        ob = Solution()
        preOrder(ob.buildTree(in_order, post_order))
        print()
        print("~")
# } Driver Code Ends