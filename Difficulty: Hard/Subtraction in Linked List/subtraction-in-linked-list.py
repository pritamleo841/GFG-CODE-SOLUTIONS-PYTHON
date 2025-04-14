#User function Template for python3

class Solution:
    '''
    1.Compare the two linked lists to determine which number is larger.
    2.Reverse both lists to simplify subtraction (start from least significant digit).    
    3.Subtract digit-by-digit with borrowing.
    4.Remove leading zeros from the result.
    5.Reverse the final result to restore proper order.
    '''
    def reverse(self,head):
        prev=None
        while head!=None:
            nnext=head.next
            head.next=prev
            prev=head
            head=nnext
        return prev
        
    def rm_leading_zeros(self,head):
        while head and head.next and head.data==0:
            head=head.next
        return head
    
    def get_length(self,head):
        count=0
        while head:
            head=head.next
            count+=1
        return count
        
    def compare_list(self,head1,head2):
        l1=self.get_length(head1)
        l2=self.get_length(head2)
        if l1!=l2:
            return l1-l2
        while head1 and head2:
            if head1.data!=head2.data:
                return head1.data-head2.data
            head1=head1.next
            head2=head2.next
        return 0
        
    def subLinkedList(self, head1, head2): 
        if self.compare_list(head1,head2)<0:
            head1,head2=head2,head1
        head1=self.reverse(head1)
        head2=self.reverse(head2)
        res_head=None
        curr=None
        borrow=0
        while head1 or head2:
            val1=head1.data if head1 else 0
            val2=head2.data if head2 else 0
            sub=val1-val2-borrow
            if sub<0:
                sub+=10
                borrow=1
            else:
                borrow=0
            new_node=Node(sub)
            if not res_head:
                res_head=curr=new_node
            else:
                curr.next=new_node
                curr=curr.next
            head1=head1.next if head1 else None
            head2=head2.next if head2 else None
        res_head=self.reverse(res_head)
        res_head=self.rm_leading_zeros(res_head)
        return res_head
        # return head of difference list



#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def print_list(head):
    """Prints the linked list."""
    while head:
        print(head.data, end='')
        head = head.next
    print()


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    index = 1
    solution = Solution()

    for _ in range(T):
        input1 = data[index]
        input2 = data[index + 1]
        index += 2

        head1, tail1 = None, None
        head2, tail2 = None, None

        # Create the linked list for input1
        for ch in input1:
            tmp = int(ch)
            new_node = Node(tmp)
            if head1 is None:
                head1 = new_node
                tail1 = new_node
            else:
                tail1.next = new_node
                tail1 = new_node

        # Create the linked list for input2
        for ch in input2:
            tmp = int(ch)
            new_node = Node(tmp)
            if head2 is None:
                head2 = new_node
                tail2 = new_node
            else:
                tail2.next = new_node
                tail2 = new_node

        result = solution.subLinkedList(head1, head2)
        print_list(result)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends