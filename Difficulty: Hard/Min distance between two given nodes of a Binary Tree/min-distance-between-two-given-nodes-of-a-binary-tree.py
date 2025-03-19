#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self,root,a,b):
        '''
            1. Find LCA of a and b
            2. Find distances from LCA,a and LCA,b
            3. Return the sum of their distances
        '''
        def lca(root, n1, n2):
            #if any of the node is found,return the node
            if not root or (root.data == n1 or root.data == n2):
                return root
            left_tree = lca(root.left,n1,n2)
            right_tree = lca(root.right,n1,n2)
            #if both subtrees return non-null values, return the root
            if left_tree and right_tree:
                return root
            #return the non-null node from a subtree
            return left_tree if left_tree else right_tree
            
        def distance(root,target,dist=0):
            if not root:
                return 
            if root.data==target:
                return dist
            return distance(root.left,target,dist+1) or distance(root.right,target,dist+1)
            
        lca_root = lca(root,a,b)
        d1=distance(lca_root,a)
        d2=distance(lca_root,b)
        return d1+d2
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(50000)
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        a = int(input())
        b = int(input())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends