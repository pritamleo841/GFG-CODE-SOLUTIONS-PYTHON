'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def distributeCandy(self, root):
        #coming up to the problem intuition is hard
        self.res = 0
        def dfs(node):
            if not node:
                return [0,0]
            l_size,l_candies=dfs(node.left)
            r_size,r_candies=dfs(node.right)
            
            size = 1+l_size+r_size
            candies=node.data+l_candies+r_candies
            self.res+=abs(size-candies)
            return [size,candies]
        dfs(root)
        return self.res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = input()
        root = buildTree(s)
        ob = Solution()
        print(ob.distributeCandy(root))

        print("~")

# } Driver Code Ends