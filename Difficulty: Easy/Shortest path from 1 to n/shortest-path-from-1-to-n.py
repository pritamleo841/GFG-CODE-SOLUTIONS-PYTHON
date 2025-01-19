#User function Template for python3
from collections import deque
class Solution:
    def minimumStep (self, n):
        #complete the function here
        
        #expected TC - O(logn)
        #we are starting from end node and traversing to start node
        ans=0
        while n>1 :
            if n%3==0:
                ans+=1
                n=n/3
            else:
                ans+=1
                n-=1
        return ans
        
        #using BFS - TLE
        #TC : O(n), SC : O(n)
        # if n == 1:
        #     return 0  # Already at the target
    
        # # Initialize BFS
        # queue = deque([(1, 0)])  # (current vertex, distance from 1)
        # visited = set()
        # visited.add(1)
        
        # while queue:
        #     current, dist = queue.popleft()
            
        #     # Generate neighbors
        #     for neighbor in (current + 1, 3 * current):
        #         if neighbor == n:
        #             return dist + 1  # Found the target
        #         if neighbor > n or neighbor in visited:
        #             continue
        #         visited.add(neighbor)
        #         queue.append((neighbor, dist + 1))
        
        # return -1  # Should not reach here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
        print("~")
# } Driver Code Ends