#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
class Solution:
    # Function to count the number of leaf nodes in a binary tree.
    def countLeaves(self, root):
       stack = [root]
       count = 0
       #preorder traversal using stack
       while stack:
           node = stack.pop()
           if not node.right and not node.left:
               count+=1
           if node.right:
               stack.append(node.right)
           if node.left:
               stack.append(node.left)
       return count


#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while q and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)

        i += 1
    return root


# Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    solution = Solution()  # Create an instance of Solution
    for _ in range(t):
        s = input()
        root = buildTree(s)  # Build the tree using the buildTree function
        print(solution.countLeaves(
            root))  # Call countLeaves on the Solution instance
        print("~")

# } Driver Code Ends