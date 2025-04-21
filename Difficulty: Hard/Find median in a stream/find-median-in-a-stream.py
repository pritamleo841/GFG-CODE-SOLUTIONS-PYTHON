import heapq
class Solution:
    def getMedian(self, arr):
        '''
        1. Max Heap (maxHeap) will store the smaller half.
        2. Min Heap (minHeap) will store the larger half.
        3. Balance both heaps such that their size difference is at most 1.
        4. The median is:
            The top of the larger heap if sizes are unequal.
            The average of both tops if sizes are equal.
        '''
        minheap=[]
        maxheap=[]
        medians=[]
        for elem in arr:
            #input in maxheap
            heapq.heappush(maxheap,-elem)
            #get top of maxheap into minheap
            heapq.heappush(minheap,-heapq.heappop(maxheap))
            #balance both heaps
            if len(minheap)>len(maxheap):
                heapq.heappush(maxheap,-heapq.heappop(minheap))
                
            if len(minheap)==len(maxheap):
                medians.append((minheap[0]-maxheap[0])/2.0)
            else:
                medians.append(-maxheap[0]*1.0)
        return medians
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends