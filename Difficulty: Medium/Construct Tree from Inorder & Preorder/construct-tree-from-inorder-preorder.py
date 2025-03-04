#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
         # HashMap to store inorder indices for O(1) lookup
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        pre_idx = 0  # Pointer for preorder traversal
        def construct(in_start, in_end):
            nonlocal pre_idx
            if in_start > in_end:
                return None
            # Pick current node from preorder
            root_value = preorder[pre_idx]
            root = Node(root_value)
            pre_idx += 1
            # Get index in inorder array
            mid = inorder_map[root_value]
            # Build left and right subtrees using indices
            root.left = construct(in_start, mid - 1)
            root.right = construct(mid + 1, in_end)
            return root

        return construct(0, len(inorder) - 1)
        '''
        # O(n^2) solution
        if not inorder or not preorder:
            return None
        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(inorder[:mid],preorder[1:mid+1])
        root.right = self.buildTree(inorder[mid+1:],preorder[mid+1:])
        return root
        '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends