#User function Template for python3
import heapq
from collections import defaultdict
class Solution:
    def kTop(self,a, N, K):
        freq=defaultdict(int)
        result = []
        top = []  # Keeps last top-K sorted list

        for i in range(N):
            val = a[i]
            freq[val] += 1

            # Add to top list if not there already
            if val not in top:
                top.append(val)

            # Sort the top list with custom logic:
            # - higher frequency first
            # - smaller number first if tie
            top.sort(key=lambda x: (-freq[x], x))

            result.append(top[:K])  # Take only top K

        return result
        '''
        result=[]
        heap=[]
        for i in range(N):
            val=a[i]
            freq[val]+=1
            heapq.heappush(heap,(-freq[val],val))
            temp_heap = heap[:]
            heapq.heapify(temp_heap)
            unique=set()
            top_k=[]
            while temp_heap and len(top_k)<K:
                count,val=heapq.heappop(temp_heap)
                if val not in unique and freq[val]==-count:
                    top_k.append(val)
                    unique.add(val)
            result.append(top_k)
        return result
        '''
        


#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



    print("~")
# } Driver Code Ends