#User function Template for python3
import heapq
class Solution:
    def maxEvents(self, start, end, N):
        events=sorted(zip(start,end)) #sort based on start day
        minHeap=[]
        count=0 #no. of events attended
        i=0 #track events
        max_day = max(end)
        for day in range(1,max_day+1):
            #Add all events starting today
            while i<N and events[i][0]==day:
                heapq.heappush(minHeap,events[i][1]) #push end day
                i+=1
            #Remove expired events
            while len(minHeap) and minHeap[0]<day:
                heapq.heappop(minHeap)
            #Attend the event that ends the earliest
            if len(minHeap):
                heapq.heappop(minHeap)
                count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        start=list(map(int,input().split()))
        end=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxEvents(start,end,N))
        print("~")
# } Driver Code Ends