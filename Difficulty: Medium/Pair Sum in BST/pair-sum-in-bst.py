#User function Template for python3


#Function to check if any pair exists in BST whose sum is equal to given value.
def findPair(root,X):
    map_x = set()
    def dfs(node):
        if not node:
           return False
        if (X-node.key) in map_x:
           return True
        map_x.add(node.key)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class:
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

hash = set() # hash to be used.
# Tree Class
class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self,x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x: # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:   #  go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return # no duplicate is to be inserted

        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)
        return

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        x = int(input())
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        if findPair(tree.root,x):
            print(1)
        else:
            print(0)
        hash = set()


        print("~")
# } Driver Code Ends