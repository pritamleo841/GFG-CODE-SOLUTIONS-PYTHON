#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def sortedListToBST(self, head):
    
        # Helper function to find the middle and split the list
        def findMiddleAndSplit(head):
            if not head or not head.next:
                return head,None  # Single element or empty list
                
            slow,fast=head,head
            prev=None  # Keeps track of the node before slow
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            if prev:
                prev.next = None  # Split the list into two parts
            return slow,head  # Middle node and left half's head

        # Recursive function to construct BST
        def createBST(head):
            if not head:
                return None
            mid,left_head=findMiddleAndSplit(head)
            root=TNode(mid.data)  # Create root with mid element

            if mid==head:  # Base case when there's only one element
                return root

            root.left=createBST(left_head)  # Left subtree
            root.right=createBST(mid.next)  # Right subtree
            return root
        
        return createBST(head)  # Call the recursive function
        
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3
# Node Class
class LNode:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class TNode:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = LNode(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list
def preOrder(root):
    if root == None:
        return

    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


if __name__ == '__main__':
    for _ in range(int(input())):

        a = LinkedList()  # create a new linked list 'a'.
        #b = LinkedList() # create a new linked list 'b'.

        nodes_a = list(map(int, input().strip().split()))
        #nodes_b = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.append(x)

        ob = Solution()
        root = ob.sortedListToBST(a.head)
        preOrder(root)

        print()

        print("~")

# } Driver Code Ends