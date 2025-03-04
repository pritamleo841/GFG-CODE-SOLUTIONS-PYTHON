#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    #O(n) method -> Striver
    index = [0]
    def build(bound):
        if index[0] >= size or pre[index[0]] > bound:
            return None
        root = Node(pre[index[0]])
        index[0] += 1  # Move to the next element
        # All elements smaller than root.data go to the left subtree
        root.left = build(root.data)
        # Remaining elements go to the right subtree
        root.right = build(bound)
        return root
        
    return build(float('inf'))


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for _tcs in range(t):
        size = int(input())
        pre = [int(x) for x in input().split()]

        root = Bst(pre, size)

        postOrd(root)
        print()

        print("~")
# } Driver Code Ends