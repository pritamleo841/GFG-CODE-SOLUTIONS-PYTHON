class Solution:
    def delete_node(self, head, x):
        
        if head is None:
            return None
        curr = head
        count = 1
        # Traverse to the x-th node (1-based indexing)
        while curr and count < x:
            curr = curr.next
            count += 1
        if curr is None:
            return head  # x is out of bounds
        # If deleting head node
        if curr.prev is None:
            head = curr.next
            if head:
                head.prev = None
        else:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
    
        return head


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = Node(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def verifyDLL(head):
    c1, c2 = 0, 0
    tmp = head
    while tmp.next:
        c1 += 1
        tmp = tmp.next
    while tmp.prev:
        c2 += 1
        tmp = tmp.prev
    return c1 == c2


def printList(head):
    if not head:
        return
    if verifyDLL(head) == False:
        return
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.delete_node(head, int(input().strip()))
        printList(resHead)
        print("~")

# } Driver Code Ends