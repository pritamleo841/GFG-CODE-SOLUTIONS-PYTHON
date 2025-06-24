# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    if arr:
        return arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    return len(arr)>=n

# function should return 1/0 or True/False
def isEmpty(arr):
    return len(arr)==0

# function should return minimum element from the stack
def getMin(n, arr):
    if arr:
        return min(arr)
    return None