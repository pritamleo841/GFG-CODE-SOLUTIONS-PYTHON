#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
    def isCousins(self,root, a, b):
        # Your code here
        if not root:
            return False
        #use bfs traversal
        queue = deque()
        queue.append((root,None,0)) #tuples [value, parent, depth]
        
        #declare parents and depth for a and b 
        parent_a = parent_b = None
        depth_a = depth_b = -1
        
        while queue:
            node, parent, depth = queue.popleft()
            #if a is found, store parent and depht of a
            if node.data == a:
                parent_a,depth_a = parent,depth
            #if b is found, store parent and depht of b
            elif node.data == b:
                parent_b,depth_b = parent,depth
            #if both parents are found, break the loop
            if parent_a and parent_b:
                break
            
            if node.left :
                queue.append((node.left,node,depth+1))
            if node.right :
                queue.append((node.right,node,depth+1))
        
        return parent_a!=parent_b and depth_a==depth_b

#{ 
 # Driver Code Starts
from collections import deque


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None

    # Creating list of strings from input string after splitting by space
    ip = s.split()

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    queue = deque([root])

    # Starting from the second element
    i = 1
    while queue and i < len(ip):

        # Get and remove the front of the queue
        currNode = queue.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            queue.append(currNode.left)

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
            queue.append(currNode.right)
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    solution = Solution()
    for _ in range(t):
        s = input().strip()
        root = buildTree(s)
        x, y = map(int, input().strip().split())
        if x == y:
            print(0)
        else:
            print(1 if solution.isCousins(root, x, y) else 0)
        print("~")

# } Driver Code Ends