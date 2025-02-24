#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def nodesAtOddLevels(self,root):
        #code here
        from collections import deque
        queue = deque([root])
        level = 1
        ans = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if level%2!=0:
                    ans.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


#Back-end complete function Template for Python 3


class Solution:

    def nodesAtOddLevels(self, root):
        oddNodes = []
        self.nodesAtOddLevelsUtil(root, 1, oddNodes)
        return oddNodes

    def nodesAtOddLevelsUtil(self, root, l, oddNodes):
        if (root == None):
            return
        if l % 2 == 1:
            oddNodes.append(root.data)
        self.nodesAtOddLevelsUtil(root.left, l + 1, oddNodes)
        self.nodesAtOddLevelsUtil(root.right, l + 1, oddNodes)


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
        v = ob.nodesAtOddLevels(root)

        v.sort()
        for i in v:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends