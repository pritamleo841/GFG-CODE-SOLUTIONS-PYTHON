#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
        


# } Driver Code Ends

#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        if not root:
            return None
        # Pointers to track head and previous node
        self.head=None
        self.prev=None

        def inorder(node):
            if not node:
                return
            # Recursively process left subtree
            inorder(node.left)
            # Convert node to CDLL
            if self.prev is None:
                # First node (leftmost), set as head
                self.head=node
            else:
                # Connect previous and current nodes
                self.prev.right=node
                node.left=self.prev
            # Update previous node pointer
            self.prev=node
            # Recursively process right subtree
            inorder(node.right)

        # Perform inorder traversal and construct DLL
        inorder(root)

        # Make it circular
        if self.head and self.prev:
            self.head.left=self.prev
            self.prev.right=self.head

        return self.head



#{ 
 # Driver Code Starts.
def displayList(head):
    itr=head
    while(itr.right!=head):
        print(itr.data,end=" ")
        itr=itr.right
    print(itr.data,end=" ")
    print()
    head = itr
    while(itr.left!=head):
        print(itr.data,end=" ")
        itr=itr.left
    print(itr.data, end=" ")
    
 
    
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
        head=Solution().bTreeToClist(root)
        displayList(head)
        print()
        
        

        




        print("~")
# } Driver Code Ends