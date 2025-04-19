#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, arr):
        minHeap = []
        for l in arr:
            current = l
            while current:
                heapq.heappush(minHeap,current.data)
                current=current.next
                
        head=tail=None
        while len(minHeap):
            val=heapq.heappop(minHeap)
            new_node = Node(val)
            if head is None:
                head=tail=new_node
            else:
               tail.next=new_node #sets next pointer to new_node
               tail=new_node #new_node becomes tail
        return head
        # return head of merged list


#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends