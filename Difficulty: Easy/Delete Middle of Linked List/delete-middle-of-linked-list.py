#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if head is None or head.next is None:
            return None
        fast=slow=head
        prev=None
        #finding middle using slow and fast pointer
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        #delete the middle
        prev.next=slow.next
        return head
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        obj = Solution()
        res = obj.deleteMid(head)
        printList(res)
        print("~")

# } Driver Code Ends