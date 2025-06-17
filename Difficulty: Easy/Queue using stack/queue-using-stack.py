class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if self.stack else -1
        
class Queue:
    def __init__(self):
        self.stack1 = Stack()  # for enqueue
        self.stack2 = Stack()  # for dequeue

    def enqueue(self, x):
        self.stack1.push(x)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
                