#User function Template for python3



'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to count number of subtrees having sum equal to given sum.
def countSubtreesWithSumX(root, x):
    #Use Postorder traversal to get subtree sum
    if not root:
        return 0
    count = 0
    def dfs(node):
        nonlocal count
        if not node:
            return 0
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        subtree_sum = left_sum+right_sum+node.data
        if subtree_sum==x:
            count+=1
        return subtree_sum
    dfs(root)
    return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(100000);
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
        x = int(input())
        print(countSubtreesWithSumX(root,x))
        
        


        print("~")
# } Driver Code Ends