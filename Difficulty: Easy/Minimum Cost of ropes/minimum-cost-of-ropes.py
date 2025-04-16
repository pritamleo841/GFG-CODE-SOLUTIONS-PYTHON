import heapq
class Solution:
   def minCost(self, arr):
        pq = []
        for i in range(len(arr)):
           heapq.heappush(pq,arr[i])
        cost=0
        while len(pq)>1:
            f = heapq.heappop(pq) if len(pq) else 0
            s = heapq.heappop(pq) if len(pq) else 0
            cost+=(f+s)
            heapq.heappush(pq,f+s)
            
        return cost
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())

    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))
        print("~")

# } Driver Code Ends