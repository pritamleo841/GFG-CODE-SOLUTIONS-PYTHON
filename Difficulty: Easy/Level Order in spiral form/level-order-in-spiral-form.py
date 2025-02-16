#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        
from collections import deque
class Solution:
    def findSpiral(self, root):
        #code here
        queue=deque([root])
        left_to_right = False #start with right to left
        res = []
        while queue:
            level_size = len(queue)
            level = deque()
            for _ in range(level_size): #process all nodes at once
                current = queue.popleft()
                if left_to_right:
                    level.append(current.data)
                else:
                    level.appendleft(current.data)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            res.extend(level)
            left_to_right = not left_to_right #reverse direction
        return res
        


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

    # Creating list of strings from input string after splitting by space
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


# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends