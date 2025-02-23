#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return the height of the given special binary tree
def findTreeHeight(root):
    # node is a leaf node or node
    def isLeaf(node):
        # For a node to be a leaf node, it should
        # satisfy the following two conditions:
        # 1. Node's left's right pointer should be 
        # current node.
        # 2. Node's right's left pointer should be 
        # current node.
        
        # If one condition is met, it is guaranteed
        # that the other condition is also true.
        return (node.left and node.left.right == node and 
                node.right and node.right.left == node)
        # if node is NULL, return -1.
    if root is None:
        return -1
    # if node is a leaf node, return 0
    if isLeaf(root):
        return 0
    # compute the depth of each subtree and take maximum
    return 1+max(findTreeHeight(root.left),findTreeHeight(root.right))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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


def saveLeafNodes(root, Leaf):
    if not root:
        return
    saveLeafNodes(root.left, Leaf)

    if not root.left and not root.right:
        Leaf.append(root)

    saveLeafNodes(root.right, Leaf)


def linkLeafNodes(root):

    Leaf = []
    saveLeafNodes(root, Leaf)

    if len(Leaf) <= 1:
        return

    for i in range(0, len(Leaf)):
        if i == 0:
            Leaf[i].right = Leaf[i + 1]
            Leaf[i].left = Leaf[len(Leaf) - 1]
        elif i == len(Leaf) - 1:
            Leaf[i].right = Leaf[0]
            Leaf[i].left = Leaf[i - 1]
        else:
            Leaf[i].right = Leaf[i + 1]
            Leaf[i].left = Leaf[i - 1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        linkLeafNodes(root)
        ans = findTreeHeight(root)
        print(ans)
        print("~")

# } Driver Code Ends