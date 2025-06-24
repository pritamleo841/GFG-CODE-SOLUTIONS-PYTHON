class TwoStacks:
    def __init__(self, size=100):
        self.arr=[None]*size
        self.top1=-1
        self.top2=size
        self.size=size

    # Push to Stack 1
    def push1(self,x):
        if self.top1+1<self.top2:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            print("Stack Overflow in Stack 1")

    # Push to Stack 2
    def push2(self, x):
        if self.top2-1>self.top1:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            print("Stack Overflow in Stack 2")

    # Pop from Stack 1
    def pop1(self):
        if self.top1>=0:
            val=self.arr[self.top1]
            self.top1-=1
            return val
        else:
            return -1  # Stack underflow

    # Pop from Stack 2
    def pop2(self):
        if self.top2<self.size:
            val=self.arr[self.top2]
            self.top2+=1
            return val
        else:
            return -1  #Stack underflow