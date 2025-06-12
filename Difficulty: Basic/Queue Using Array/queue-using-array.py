class MyQueue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
    #Function to push an element x in a queue.
    def push(self, x):
         self.in_stack.append(x)
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        else:
            return -1
         # add code here