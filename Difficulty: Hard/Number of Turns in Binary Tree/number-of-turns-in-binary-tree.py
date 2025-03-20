#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def NumberOFTurns(self, root, first, second):
        # Find LCA of first and second
        def lca(root, n1, n2):
            if not root:
                return None
            if root.data == n1 or root.data == n2:
                return root
            left = lca(root.left, n1, n2)
            right = lca(root.right, n1, n2)
            if left and right:
                return root
            return left if left else right

        # Helper function to check if a node exists in the tree
        def nodeExists(root, key):
            if not root:
                return False
            if root.data == key:
                return True
            return nodeExists(root.left, key) or nodeExists(root.right, key)

        # Find number of turns from root to target
        def countTurns(root, target, prev_dir, turns):
            if not root:
                return 0, False
            if root.data == target:
                return turns, True

            if prev_dir == 'left':
                left_turn, found_left = countTurns(root.left, target, 'left', turns)
                if found_left:
                    return left_turn, True
                right_turn, found_right = countTurns(root.right, target, 'right', turns + 1)
                if found_right:
                    return right_turn, True
            else:
                right_turn, found_right = countTurns(root.right, target, 'right', turns)
                if found_right:
                    return right_turn, True
                left_turn, found_left = countTurns(root.left, target, 'left', turns + 1)
                if found_left:
                    return left_turn, True

            return 0, False

        # Step 1: Check if nodes exist in the tree
        if not nodeExists(root, first) or not nodeExists(root, second):
            return -1  # If either node is missing, return -1

        # Step 2: Find LCA
        root_lca = lca(root, first, second)
        if not root_lca:
            return -1  

        # Step 3: Count turns from LCA to both nodes
        left_turn, found1 = countTurns(root_lca.left, first, 'left', 0)
        right_turn, found2 = countTurns(root_lca.right, first, 'right', 0)

        left_turn2, found3 = countTurns(root_lca.left, second, 'left', 0)
        right_turn2, found4 = countTurns(root_lca.right, second, 'right', 0)

        # Step 4: Compute total turns
        total_turns = left_turn + right_turn + left_turn2 + right_turn2

        # If the nodes are in separate subtrees, add 1 turn at the LCA
        if (found1 or found2) and (found3 or found4):
            total_turns += 1

        return total_turns

        

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
        n1,n2=list(map(int, input().strip().split())) 
        ob = Solution()
        turn = ob.NumberOFTurns(root,n1,n2)
        if turn!=0:
            print(turn)
        else:
            print(-1)
        print("~")
# } Driver Code Ends