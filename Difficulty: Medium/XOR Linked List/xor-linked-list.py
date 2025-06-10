class Node:
    def __init__(self,x):
        data = x
        npx = NULL

def XOR(a, b):
    return a ^ b if a and b else a or b
    
def insert(head, data):
    ptr=Node(data)
    if head is None:
       head=ptr
    else:
        ptr.npx=head
        head=ptr
    return ptr

def getList(head):
    ans=[]
    while head != None:
        ans.append(head.data)
        head=head.npx
    return ans