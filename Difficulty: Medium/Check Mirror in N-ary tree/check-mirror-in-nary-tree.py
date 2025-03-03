class StackMap:
    def __init__(self):
        self.stack_map = {}
    # Function to push an element to a stack at a specific index
    def push(self,index, value):
        if index not in self.stack_map:
            self.stack_map[index] = []  # Initialize stack if not present
        self.stack_map[index].append(value)  # Push value to stack
    # Function to pop an element from a stack at a specific index
    def pop(self,index):
        if index in self.stack_map and self.stack_map[index]:  # Ensure stack exists and is not empty
            return self.stack_map[index].pop()
        return None  # Return None if stack is empty or does not exist
     # Function to get the top element of a stack at a specific index
    def top(self, index):
        if index in self.stack_map and self.stack_map[index]:
            return self.stack_map[index][-1]  # Return top element
        return None
        
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        mp = StackMap()
        for i in range(0,2*e,2):
            mp.push(A[i],A[i+1])
        
        for i in range(0,2*e,2):
            if mp.top(B[i])!=B[i+1]:
                return 0
            mp.pop(B[i])
        return 1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.checkMirrorTree(n,e,A,B))
        print("~")
# } Driver Code Ends