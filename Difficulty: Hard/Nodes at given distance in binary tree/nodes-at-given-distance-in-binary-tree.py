#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    def KDistanceNodes(self,root,target,k):
        #Finds the target node and stores parent pointers.
        def locate_target(node,target):
            if not node:
                return None
            if node.data==target:
                return node
            parent_map[node.left]=node
            parent_map[node.right]=node
            return locate_target(node.left,target) or locate_target(node.right,target)
        #Finds all nodes at distance k from the given node.
        def find_K_nodes(node,k,visited,result):
            if not node or k<0 or node in visited:
                return
            visited.add(node)
            if k==0:
                result.append(node.data)
                return
            find_K_nodes(node.left,k-1,visited,result)
            find_K_nodes(node.right,k-1,visited,result)
            find_K_nodes(parent_map.get(node),k-1,visited,result)

        # Step 1: Build parent pointers
        parent_map = {}
        parent_map[root] = None  # Root has no parent
        target_node = locate_target(root,target)
        if not target_node:
            return []

        # Step 2: Find nodes at distance K
        result = []
        find_K_nodes(target_node,k,set(),result)
        
        return sorted(result)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque, defaultdict


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
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
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target = int(input())
        k = int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root, target, k)

        for i in res:
            print(i, end=' ')
        print()

        print("~")

# } Driver Code Ends