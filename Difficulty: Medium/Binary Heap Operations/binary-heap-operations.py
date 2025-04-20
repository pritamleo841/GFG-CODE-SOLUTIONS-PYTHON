#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
# Helper to swap
def swap(i, j):
    heap[i], heap[j] = heap[j], heap[i]

# Helper to heapify up
def heapify_up(i):
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        swap(i, (i - 1) // 2)
        i = (i - 1) // 2

# Helper to heapify down
def heapify_down(i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < curr_size and heap[left] < heap[smallest]:
        smallest = left
    if right < curr_size and heap[right] < heap[smallest]:
        smallest = right
    if smallest != i:
        swap(i, smallest)
        heapify_down(smallest)
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size
    heap[curr_size] = x
    heapify_up(curr_size)
    curr_size += 1

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    if i >= curr_size:
        return
    # Replace ith element with last element
    heap[i] = heap[curr_size - 1]
    curr_size -= 1
    # Try both up and down heapify
    heapify_up(i)
    heapify_down(i)

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size == 0:
        return -1
    minimum = heap[0]
    heap[0] = heap[curr_size - 1]
    curr_size -= 1
    heapify_down(0)
    return minimum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
        print("~")
# } Driver Code Ends