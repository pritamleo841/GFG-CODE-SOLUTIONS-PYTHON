class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        #add code here
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr)>0:
            return self.arr.pop()
        else:
            return -1
        #add code here
        
        