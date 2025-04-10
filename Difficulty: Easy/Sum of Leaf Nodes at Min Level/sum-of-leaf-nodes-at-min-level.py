#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def minLeafSum(self,root):
        #code here
        from collections import deque
        # BFS approach to find sum of minimum-level leaf nodes
        queue = deque([root])
        while queue:
            leaf_sum = 0  # Reset sum at each level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node is None:
                    continue
                # If node is a leaf, add to sum
                if not node.left and not node.right:
                    leaf_sum += node.data
                # Continue BFS traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Stop BFS if we found leaf nodes at the current level
            if leaf_sum > 0:
                return leaf_sum
        return 0  # In case tree is empty (edge case)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.minLeafSum(root)
        print(res)

        print("~")
# } Driver Code Ends