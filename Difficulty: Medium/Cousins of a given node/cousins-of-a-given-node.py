#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    def printCousins(self, root, node_to_find):
        if not root or not node_to_find:
            return [-1]

        queue = deque([(root, None)])
        cousins = []
        found = False
        node_to_be_find_parent = None

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                curr_node, curr_parent = queue.popleft()
                level_nodes.append((curr_node, curr_parent))

                if curr_node.data == node_to_find.data:
                    found = True
                    node_to_be_find_parent = curr_parent

                if curr_node.left:
                    queue.append((curr_node.left, curr_node))
                if curr_node.right:
                    queue.append((curr_node.right, curr_node))

            if found:
                for node, parent in level_nodes:
                    if node.data != node_to_find.data and parent != node_to_be_find_parent:
                        if parent is None and node_to_be_find_parent is None:
                            continue
                        elif parent is not None and node_to_be_find_parent is not None:
                            if parent.data != node_to_be_find_parent.data:
                                cousins.append(node.data)
                        else:
                            cousins.append(node.data)
                return cousins if cousins else [-1]

        return [-1]  



#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
    if(len(s)==0 or s[0]=="N"):
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
def pointer(root, n):
    if root == None:
        return None
    
    if root.data == n:
        return root
        
    l= pointer(root.left, n)
    if l != None and l.data==n :
        return l
    
    r= pointer(root.right, n)
    return r
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n=int(input())
        s=input()
        root = buildTree(s)
        p = pointer(root, n)
        ob = Solution()
        ans = ob.printCousins(root, p)
        
        for i in range(len(ans)):
           print(ans[i], end=" ")
                
        print()
            
# } Driver Code Ends