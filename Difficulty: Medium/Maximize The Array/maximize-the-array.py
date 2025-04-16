#User function Template for python3
import heapq
class Solution:
    def maximizeArray(self, arr1, arr2, n):
        #Get elements in max-heap
        pq=[]
        for i in range(n):
            heapq.heappush(pq,-arr2[i])
            heapq.heappush(pq,-arr1[i])
        #Get n unique elements from max-heap to set   
        seen=set()
        while len(seen)!=n:
            elem = -heapq.heappop(pq)
            seen.add(elem)
        #First pick elements from arr2 then from arr1 that are in set   
        res=[]
        for elem in arr2:
            if elem in seen:
                res.append(elem)
                seen.remove(elem)
        for elem in arr1:
            if elem in seen:
                res.append(elem)
                seen.remove(elem)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1

        print("~")
# } Driver Code Ends