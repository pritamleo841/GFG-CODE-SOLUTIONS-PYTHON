#User function Template for python3
import heapq
class Solution:
    def kthLargest(self, k, arr, n):
        '''
        1.If heap size exceeds k, pop the smallest (to retain only top k elements).
        2.If heap size is less than k, append -1 to result.
        3.If heap size is k, the root is the kth largest → append heap[0] to result.
        '''
        minheap = []
        res= []
        for elem in arr:
            heapq.heappush(minheap,elem)
            if len(minheap)<k:
                res.append(-1)
            # always stores exactly k elements,and its root is the Kth largest.
            elif len(minheap)==k:
                res.append(minheap[0])
            else:
                heapq.heappop(minheap)
                res.append(minheap[0])
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(*ob.kthLargest(k,arr,n))
        print("~")
# } Driver Code Ends