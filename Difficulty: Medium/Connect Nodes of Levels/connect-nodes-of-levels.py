#User function Template for python3

import sys
sys.setrecursionlimit(50000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        if not root:
            return None
        from collections import deque
        queue=deque([root])
        while queue:
            prev=None
            #level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.nextRight=node
                prev=node #update previous node for next iteration
                #level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #last node will always be null at a level
            prev.nextRight=None        
            '''for i in range(len(level_nodes)-1):
                level_nodes[i].nextRight=level_nodes[i+1]
            level_nodes[-1].nextRight=None
            '''
        return root
                    
        




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
        self.nextRight = None


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


def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None:  # check if the root is none
        return
    InOrder(root.left)  # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right)  # do in order of right child


def printSpecial(root):
    if root == None:
        return
    next_root = None
    while root != None:
        print(root.data, end=" ")
        if root.left and not next_root:
            next_root = root.left
        elif root.right and not next_root:
            next_root = root.right
        root = root.nextRight
    printSpecial(next_root)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        obj.connect(root)
        printSpecial(root)
        print()
        InOrder(root)
        print()

        print("~")

# } Driver Code Ends