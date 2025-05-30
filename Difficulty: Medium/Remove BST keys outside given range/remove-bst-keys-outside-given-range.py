#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def removekeys(self, root, l, r):
        #find inorder to get sorted array from bst
        def inorder(node,arr):
            if not node:
                return
            inorder(node.left,arr)
            if l<=node.data<=r:
                arr.append(node.data)
            inorder(node.right,arr)
        #construct bst using divide and conquer approach
        def buildBalancedTree(arr,start,end):
            if start>end:
                return None
            mid=(start+end)//2
            root=Node(arr[mid])
            root.left = buildBalancedTree(arr,start,mid-1)
            root.right = buildBalancedTree(arr,mid+1,end)
            return root
        #construct balanced tree
        nodes = []
        inorder(root,nodes)
        return buildBalancedTree(nodes,0,len(nodes)-1)
            


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
    
def printInorder(root): 
  
    if root: 
        # First recur on left child 
        printInorder(root.left) 
        # then print the data of node 
        print(root.data, end=" ")
        # now recur on right child 
        printInorder(root.right) 
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        l=inp[0]
        r=inp[1]
        
        s=input()
        root=buildTree(s)
        ob=Solution()
        head = ob.removekeys(root,l,r)
        printInorder(head)
        print()
        print("~")
# } Driver Code Ends