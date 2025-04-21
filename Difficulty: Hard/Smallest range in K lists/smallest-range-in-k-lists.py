#User function Template for python3
import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        length = len(KSortedArray)
        left = right = KSortedArray[0][0]  # Initialize with a large number
        min_heap = []
        
        # Initialize left and right boundaries
        for i in range(length):
            l = KSortedArray[i]
            left = min(left, l[0])  # Set left as the minimum of the first element of each list
            right = max(right, l[0])  # Set right as the maximum of the first element of each list
            heapq.heappush(min_heap, (l[0], i, 0))  # (value, list index, element index)

        res = [left, right]  # Initialize the result with the current range
        while True:
            num, li, idx = heapq.heappop(min_heap)  # Get the smallest element in the heap
            idx += 1  # Move to the next element in the list
            if idx == len(KSortedArray[li]):  # If any list is exhausted, break
                break
            next_val = KSortedArray[li][idx]  # Get the next element in the list
            heapq.heappush(min_heap, (next_val, li, idx))  # Push the next element into the heap
            right = max(right, next_val)  # Update the right boundary to be the largest element

            # Update left boundary to be the minimum value in the heap
            left = min_heap[0][0]  # Get the smallest element from the heap

            # Update result if we find a smaller range
            if right - left < res[1] - res[0]:
                res = [left, right]

        return res  
        
        # print the smallest range in a new line


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
    print("~")
# } Driver Code Ends