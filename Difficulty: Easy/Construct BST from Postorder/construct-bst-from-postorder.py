#User function Template for python3

class Solution:
    def constructTree(self,postorder,n):
        # code here
        if not postorder:
            return None
        # Start with the last element as the root
        root=Node(postorder[-1])
        stack=[root]
        # Traverse postorder from right to left (backward)
        for i in range(len(postorder)-2,-1,-1):
            node=Node(postorder[i])
            parent=None
            # Find the correct parent for this node
            while stack and postorder[i]<stack[-1].val:
                parent=stack.pop()
            # If parent is found, this node is the left child
            if parent:
                parent.left=node
            else:
                # Otherwise, it's the right child of the last stacked node
                stack[-1].right=node
            # Push this node onto the stack
            stack.append(node)
        return root


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
   def __init__(self,val):
       self.val=val
       self.left=None
       self.right=None
class BST:
   size=0
   def inorder(self,tmp,size=0):
       if tmp:
           self.inorder(tmp.left,self.size)
           print(tmp.val,end=" ")
           self.inorder(tmp.right,self.size)
     
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        b=BST()
        pt=obj.constructTree(arr,n)
        b.inorder(pt)
        print()

# } Driver Code Ends