#User function Template for python3
from collections import deque

class Solution:
    def minTime(self, root, target):
        if not root:
            return 0
        
        parent_map = {}  # Stores child->parent mapping
        targetNode = None  # Stores reference to target node

        # Function to map parents and find the target node
        def MapParentsAndFindTargetNode(root, target): 
            nonlocal targetNode  # Ensure modification of outer targetNode
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node.data == target:
                    targetNode = node  # Update the target node reference
                if node.left:
                    parent_map[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent_map[node.right] = node
                    queue.append(node.right)

        MapParentsAndFindTargetNode(root, target)
        if not targetNode:
            return 0  # If target is not found, return 0
        
        # Run BFS to calculate the burn time
        queue = deque([targetNode])
        visited = set()
        visited.add(targetNode)
        time = 0
        
        while queue:
            size = len(queue)
            burned = False

            for _ in range(size):  # Multi-source BFS
                node = queue.popleft()
                for neighbor in [node.left, node.right, parent_map.get(node)]:
                    if neighbor and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        burned = True  # Mark that at least one node is burned
            
            if burned:
                time += 1  # Increase time only if any new nodes burned
        
        return time
        
        
        
            
        
        



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

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

        print("~")
# } Driver Code Ends