#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def getCount(self,root,n):
        #code here
        from collections import deque
        queue=deque([(root,1)])
        leaf_levels = []
        while queue:
            node,level = queue.popleft()
            if not node.left and not node.right:
                leaf_levels.append(level)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        #sort to get the minimum cost leaf levels first
        leaf_levels.sort()
        #visit leaves in the cheapest order while staying within budget
        count, total_cost = 0, 0
        for cost in leaf_levels:
            if total_cost + cost > n:
                break  # Stop if we exceed the budget
            total_cost += cost
            count += 1

        return count
                


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
def inord(root):
    if not root:
        return
    inord(root.left)
    print(root.data,end=' ')
    inord(root.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        k = int(input());
        root=buildTree(s)
        ob = Solution()
        res = ob.getCount(root,k)
        print(res)
        print("~")
# } Driver Code Ends