#User function Template for python3
'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        fast = slow = head
        # Move fast pointer k steps ahead
        for _ in range(k):
            if not fast:
                return -1  # k is larger than the list length
            fast = fast.next
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data if slow else -1
        
        '''
        #modifies the list - improve solution
        def reverseList(head):
            prev=None
            curr=head
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        new_head = reverseList(head)
        count=1
        while new_head:
            if count==k:
                return new_head.data
            new_head=new_head.next
            count+=1
        return -1
        '''
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        print(ob.getKthFromLast(head, x))
        t -= 1
        print("~")

# } Driver Code Ends