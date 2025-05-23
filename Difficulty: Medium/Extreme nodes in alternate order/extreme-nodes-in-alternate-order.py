from collections import deque
class Solution:
    # Your task is to complete this function
    def extremeNodes(self, root):
        queue=deque([root])
        level = 1
        ans=[]
        while queue:
            level_nodes = []
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                level_nodes.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level%2==0:
                ans.append(level_nodes[0])
            else:
                ans.append(level_nodes[-1])
            level+=1
        return ans


#{ 
 # Driver Code Starts
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def PreOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None:  # check if the root is none
        return
    print(root.data, end=" ")  # print root of the given tree
    PreOrder(root.left)  # do pre order of left child
    PreOrder(root.right)  # do pre order of right child


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
        nodes = Solution().extremeNodes(root)
        for node in nodes:
            print(node, end=' ')
        print()

        print("~")

# } Driver Code Ends