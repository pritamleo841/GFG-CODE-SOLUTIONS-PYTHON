#User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
from collections import defaultdict
class Solution:
    def dupSub(self, root):
        # Function which checks all the subtree of size 2 or 
        # 3 if they are duplicate.
        def dupSubRecur(root, s, ans):
            # For null nodes,
            if root is None:
                return "N"
            # For leaf nodes, return its value in string.
            if root.left is None and root.right is None:
                return str(root.data)
            curr = str(root.data)
            # Process the left and right subtree.
            left = dupSubRecur(root.left, s, ans)
            right = dupSubRecur(root.right, s, ans)
            # If the node is parent to 2 
            # leaf nodes, or 1 leaf node and 1 
            # null node, then concatenate the strings
            if left != "" and right != "":
                curr += '*' + left + '*' + right
            else:
                return ""
            # If this subtree string is already 
            # present in set, set ans to 1.
            if curr in s:
                ans[0] = 1
            else:
                s.add(curr)
            return ""
            
        ans = [0]
        s = set()
        dupSubRecur(root, s, ans)
        return ans[0]


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
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.dupSub(root))
        print("~")
# } Driver Code Ends