#User function Template for python3

''' structure of list node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self, head1, head2):
        dummy=Node(0)
        tail=dummy
        unique=set()
        result_set=set()
        while head2:
            unique.add(head2.data)
            head2=head2.next
        while head1:
            if head1.data in unique and head1.data not in result_set:
                tail.next=Node(head1.data)
                tail=tail.next
                result_set.add(head1.data)
            head1=head1.next
        
        return dummy.next
            
        
            
        
                


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    T = int(data[index])
    index += 1

    for _ in range(T):
        head1 = None
        tail1 = None
        head2 = None
        tail2 = None

        # Read the first linked list
        input1 = data[index].strip()
        index += 1
        if input1:
            elements1 = list(map(int, input1.split()))
            for tmp in elements1:
                new_node = Node(tmp)
                if head1 is None:
                    head1 = tail1 = new_node
                else:
                    tail1.next = new_node
                    tail1 = tail1.next

        # Read the second linked list
        input2 = data[index].strip()
        index += 1
        if input2:
            elements2 = list(map(int, input2.split()))
            for tmp in elements2:
                new_node = Node(tmp)
                if head2 is None:
                    head2 = tail2 = new_node
                else:
                    tail2.next = new_node
                    tail2 = tail2.next

        # Compute intersection and print result
        obj = Solution()
        result = obj.findIntersection(head1, head2)
        print_list(result)

# } Driver Code Ends