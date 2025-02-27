class Solution:
    def findMedian(self, root):
        # code here
        if not root:
            return None
        inorder = []
        def inorderDfs(node):
            if node:
                inorderDfs(node.left)
                inorder.append(node.data)
                inorderDfs(node.right)
        inorderDfs(root)
        count = len(inorder)
        # Step 2: Find median
        if count%2==1:
            return inorder[count//2]  # Odd case
        else:
            median=(inorder[count//2-1]+inorder[count//2])/2  # Even case
            return int(median) if median.is_integer() else median  # Convert to int if no decimal part
        



#{ 
 # Driver Code Starts
from collections import deque


class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1
        # For the right child
        i += 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1
        i += 1
    return root


# Main driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        solution = Solution()
        print(solution.findMedian(root))
        print("~")

# } Driver Code Ends