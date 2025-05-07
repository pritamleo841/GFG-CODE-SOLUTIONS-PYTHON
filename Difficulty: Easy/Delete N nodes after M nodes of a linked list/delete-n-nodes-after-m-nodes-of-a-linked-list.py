# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        curr=head
        while curr:
            #skip m nodes
            for i in range(1,m):
                if curr is None:
                    return head
                curr=curr.next
            if curr is None:
                return head
            #start deleting next n nodes
            temp=curr.next
            for i in range(n):
                if temp is None:
                    break
                temp=temp.next
            #connect the m-th node to the (m+n+1)-th node
            curr.next=temp
            curr=temp
        return head



#{ 
 # Driver Code Starts
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")  # Newline after printing the linked list


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()
        values = input().strip().split()
        for i in reversed(values):  # Reversed input list to preserve order
            llist.push(i)
        n, m = map(int, input().strip().split())  # n: keep, m: delete
        Solution().linkdelete(llist.head, n,
                              m)  # Call the method to modify the list
        llist.printList()
        t -= 1
        print("~")  # Separator for test cases

# } Driver Code Ends