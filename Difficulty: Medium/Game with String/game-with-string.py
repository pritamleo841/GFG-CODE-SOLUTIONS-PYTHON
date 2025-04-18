#User function Template for python3
from collections import Counter
import heapq
class Solution:
    def minValue(self, s, k):
        #Count frequency of each character
        dictm=Counter(s)
        #Create a max-heap based on frequency
        pq = [-value for value in dictm.values()]
        heapq.heapify(pq)
        #Remove k characters by reducing the highest frequency
        while k and len(pq):
            top=-heapq.heappop(pq)
            top-=1
            k-=1
            if top>0:
                heapq.heappush(pq,-top)
        return sum(x*x for x in map(lambda x:-x,pq))
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
        print("~")
# } Driver Code Ends