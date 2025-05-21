#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
       '''
       Reverse a doubly linked list, we need to:
            1.Swap the prev and next pointers of each node.
            2.Update the head to the last node we visit.
       '''
       if not head:
           return None
       curr=head
       temp=None
       while curr:
           #Swap the prev and next pointers of each node
           temp = curr.prev
           curr.prev=curr.next
           curr.next=temp
           #Move to the next node (which is previous before swap)
           curr=curr.prev #after swapped
           
       #After the loop,temp will be pointing to the node before new head
       if temp:
           head=temp.prev
       return head 



#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = DLLNode(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.reverseDLL(head)
        printList(resHead)
        print("~")

# } Driver Code Ends