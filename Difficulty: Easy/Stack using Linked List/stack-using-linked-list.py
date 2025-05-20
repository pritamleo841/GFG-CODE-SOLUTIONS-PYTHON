class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None  # No dummy node

    # Push data onto the stack
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.head
        self.head = new_node

    # Pop data from the stack
    def pop(self):
        if not self.head:
            return -1  # Stack underflow
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data



#{ 
 # Driver Code Starts
class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()
        print("~")

# } Driver Code Ends