'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
from collections import deque
class Solution:
    def maxGCD(self, root):
        # code here
        # Helper function to compute GCD using Euclidean Algorithm
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)
            
        queue = deque([root])
        max_gcd_value = 0
        max_gcd_parent = 0
        while queue:
            node = queue.popleft()
            # Check if the node has two children
            if node.left and node.right:
                current_gcd = gcd(node.left.data, node.right.data)
                # Update max GCD and its parent node
                if current_gcd > max_gcd_value:
                    max_gcd_value = current_gcd
                    max_gcd_parent = node.data
                # If the GCD values are the same, choose the larger parent node
                elif current_gcd == max_gcd_value:
                    max_gcd_parent = max(max_gcd_parent, node.data)

            # Add children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return max_gcd_parent
            
            
        
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
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.maxGCD(root))
        
        


        print("~")
# } Driver Code Ends