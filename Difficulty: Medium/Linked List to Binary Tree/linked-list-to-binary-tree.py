# User function Template for python3

'''
# Linked List node
class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

# Tree Node structure
class Tree:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

#Function to make binary tree from linked list.
from collections import deque
class Solution:
    def linkedListToBinaryTree(self, head):
        if not head:
            return None
        root = Tree(head.data)
        queue=deque([root])
        head=head.next #next node
        #construct tree level-wise
        while head:
            parent = queue.popleft()
            #Left Child
            left_child = Tree(head.data)
            parent.left = left_child
            queue.append(parent.left)
            head = head.next #next node
            #Right Child
            if head:
                right_child = Tree(head.data)
                parent.right = right_child
                queue.append(parent.right)
                head = head.next
        return root
        



#{ 
 # Driver Code Starts
# Initial Template for Python 3


# Linked List node
class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):
        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new node
        self.head = new_node

    def levelorderTraversal(self, root):
        mylist = []  # List of nodes
        if root is None:
            return
        que = []
        que.append(root)
        while que:
            node = que.pop(0)
            mylist.append(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        # Printing the list in reverse order
        print(*mylist[::-1])


if __name__ == '__main__':
    test_cases = int(input())  # Number of test cases
    solution = Solution()  # Create Solution instance

    for _ in range(test_cases):
        # Read linked list elements
        a = list(map(int, input().strip().split()))
        mylist = Conversion()  # Create linked list for each test case
        for item in a:
            mylist.push(item)  # Push elements into the linked list

        # Convert the linked list to binary tree
        root = solution.linkedListToBinaryTree(mylist.head)

        # Perform level order traversal on the binary tree
        mylist.levelorderTraversal(root)

# } Driver Code Ends