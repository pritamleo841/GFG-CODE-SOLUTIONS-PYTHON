from collections import deque
class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def checkBST(node,min_val,max_val):
            if not node:
                return True
            if not (min_val<node.data<max_val):
                return False
            return checkBST(node.left,min_val,node.data) and checkBST(node.right,node.data,max_val)
        
        return checkBST(root,float('-inf'),float('inf'))
        


#{ 
 # Driver Code Starts
from collections import deque
import sys

sys.setrecursionlimit(10**8)


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    q = deque()
    q.append(root)
    i = 1

    while i < len(ip):
        currNode = q.popleft()
        if ip[i] != "N":
            currNode.left = Node(int(ip[i]))
            q.append(currNode.left)
        i += 1
        if i < len(ip) and ip[i] != "N":
            currNode.right = Node(int(ip[i]))
            q.append(currNode.right)
        i += 1

    return root


# Main code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        if Solution().isBST(root):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends