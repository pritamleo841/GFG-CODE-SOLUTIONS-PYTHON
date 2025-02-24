class Solution:
    def RemoveHalfNodes(self, node):
        '''
        1.Recursively traverse the tree.
        2.Check each node:
            If a node has two children, return it as it is.
            If a node has only one child, return that child (effectively removing the half node).
            If a node is a leaf, return it.
        3.Modify the tree in place, returning the modified subtree.
        '''
        #code here
        def dfs(root):
            # Base case: If root is None, return None
            if not root:
                return None
            # Recursively process left and right subtrees
            root.left = dfs(root.left)
            root.right = dfs(root.right)
             # If the node is a half node with only left child, return the left child
            if root.left and not root.right:
                return root.left
            # If the node is a half node with only right child, return the right child
            if root.right and not root.left:
                return root.right
            # If it's a full node (two children), return it as is
            return root
        return dfs(node)


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = Node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while len(queue) > 0 and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)

        i += 1

    return root


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1

    while t > 0:
        s = data[index]
        root = buildTree(s)
        solution = Solution()
        fresh = solution.RemoveHalfNodes(root)
        printInorder(fresh)
        print()
        t -= 1
        index += 1
        print("~")

# } Driver Code Ends