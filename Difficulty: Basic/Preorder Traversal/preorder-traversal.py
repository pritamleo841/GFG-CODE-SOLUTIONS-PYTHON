#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        #+ab 
        #Rescursive implementation of preorder
        result = []
        def dfs(root):
            if not root:
                return None
            result.append(root.data)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result
    # code here


#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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
    while i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        if ip[i] != "N":
            currNode.left = Node(int(ip[i]))
            q.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        if ip[i] != "N":
            currNode.right = Node(int(ip[i]))
            q.append(currNode.right)

        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    solution = Solution()  # Create an instance of Solution
    for _ in range(t):
        s = input()
        root = buildTree(s)  # Build the tree using the external function
        res = solution.preorder(root)  # Get the preorder traversal
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends