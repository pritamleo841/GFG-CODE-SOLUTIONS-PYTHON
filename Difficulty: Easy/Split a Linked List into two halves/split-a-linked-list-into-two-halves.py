#User function Template for python3
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def splitList(self, head):
        slow = head
        fast = head
        if head is None:
            return None, None
        # For odd nodes, fast->next is head and 
        # for even nodes, fast->next->next is head
        #circular linked list middle finding condition
        while fast.next != head and fast.next.next != head:
            fast = fast.next.next
            slow = slow.next
        # If there are even elements in list then move fast
        if fast.next.next == head:
            fast = fast.next
        # Set the head pointer of first half
        head1 = head
        # Set the head pointer of second half
        head2 = slow.next
        # Make second half circular
        fast.next = slow.next
        # Make first half circular
        slow.next = head
    
        return head1, head2



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is not None:
        temp = head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == head:
                break
        print()


def newNode(key):
    temp = Node(key)
    return temp


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        if not arr:
            continue
        head = Node(arr[0])
        temp = head
        for number in arr[1:]:
            temp.next = Node(number)
            temp = temp.next
        temp.next = head
        ob = Solution()
        head1, head2 = ob.splitList(head)
        printList(head1)
        printList(head2)

# } Driver Code Ends