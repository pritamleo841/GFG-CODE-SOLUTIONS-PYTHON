#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def singlevalued(self, root):
        #code here
        count = 0
        def postorder(node):
            nonlocal count
            if not node:
                return True, None  # Return True (valid subtree), None (no data)
            
            left_is_uni, left_val = postorder(node.left)
            right_is_uni, right_val = postorder(node.right)
            
            # Check if the current subtree is single-valued
            if left_is_uni and right_is_uni and \
               (left_val is None or left_val == node.data) and \
               (right_val is None or right_val == node.data):
                
                count += 1
                return True, node.data  # Return True and node value
            
            return False, node.data  # Return False (not a single-valued subtree)
            
        postorder(root)
        return count
        


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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        ans = ob.singlevalued(root)
        print(ans)
        

        print("~")
# } Driver Code Ends