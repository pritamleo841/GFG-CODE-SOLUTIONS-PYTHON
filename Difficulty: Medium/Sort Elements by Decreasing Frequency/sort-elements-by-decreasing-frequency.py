#User function Template for python3
import heapq
class Solution:
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        freq={}
        for elem in arr:
            freq[elem]=freq.get(elem,0)+1
        max_heap=[(-val,key) for key,val in freq.items()]
        heapq.heapify(max_heap)
        result=[]
        while max_heap:
            value,key=heapq.heappop(max_heap)
            result.extend([key]*(-value))
        return result
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)
        print("~")

# } Driver Code Ends