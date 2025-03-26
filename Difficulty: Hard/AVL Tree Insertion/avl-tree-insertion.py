#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    #get height of a node
    def findHeight(self,node):
        if not node:
            return 0
        return node.height
    #get balance factor of a node
    def balanceFactor(self,node):
        if not node:
            return 0
        return self.findHeight(node.left)-self.findHeight(node.right)
    #right rotation(z>y>x)
    #Make Y the new root. Move Z to the right of Y. Move Y's right subtree (T3) to Z's left.
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        
        y.right=z
        z.left=T3
        
        z.height=1+max(self.findHeight(z.left),self.findHeight(z.right))
        y.height=1+max(self.findHeight(y.left),self.findHeight(y.right))
        
        return y
    #left rotation(z<y<x)
    #Make Y the new root. Move Z to the left of Y. Move Y's left subtree (T2) to Z's right.
    def leftRotate(self,z):
        y=z.right
        T3=y.left
        
        y.left=z
        z.right=T3
        
        z.height=1+max(self.findHeight(z.left),self.findHeight(z.right))
        y.height=1+max(self.findHeight(y.left),self.findHeight(y.right))
        
        return y
    # add key to AVL (if it is not present already)
    # return root node
    def insertToAVL(self, node, key):
        # Step 1: Standard BST Insert
        if not node:
            return Node(key)
        
        if key<node.data:
            node.left = self.insertToAVL(node.left,key)
        elif key>node.data:
            node.right = self.insertToAVL(node.right,key)
        else:
            return node  # Duplicate keys are not allowed

        # Step 2: Update Height
        node.height=1+max(self.findHeight(node.left),self.findHeight(node.right))

        # Step 3: Get Balance Factor
        balance=self.balanceFactor(node)

        # Step 4: Perform Rotations if Unbalanced
        # Case 1: Left-Left (Right Rotation)
        if balance>1 and key<node.left.data:
            return self.rightRotate(node)

        # Case 2: Right-Right (Left Rotation)
        if balance<-1 and key>node.right.data:
            return self.leftRotate(node)

        # Case 3: Left-Right (Left-Right Rotation)
        if balance>1 and key>node.left.data:
            node.left=self.leftRotate(node.left)
            return self.rightRotate(node)

        # Case 4: Right-Left (Right-Left Rotation)
        if balance<-1 and key<node.right.data:
            node.right=self.rightRotate(node.right)
            return self.leftRotate(node)

        return node  # Return unchanged node
            
            
            
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

        print("~")
# } Driver Code Ends