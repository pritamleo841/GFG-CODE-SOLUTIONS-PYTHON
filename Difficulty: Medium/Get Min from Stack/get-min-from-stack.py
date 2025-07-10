
class Solution:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    # Add an element to the top of Stack
    def push(self,x):
        self.stack.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.stack:
            return -1
        x=self.stack.pop()
        if x==self.min_stack[-1]:
            self.min_stack.pop()
        return x

    # Returns top element of Stack
    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    # Finds minimum element of Stack
    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]