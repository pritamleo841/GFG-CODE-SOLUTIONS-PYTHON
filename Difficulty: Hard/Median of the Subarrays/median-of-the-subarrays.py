#User function Template for python3
from collections import defaultdict
'''
To find how many subarrays have a median equal to M, we:
    Count how many subarrays have median ≥ M
    Subtract how many subarrays have median > M

This works because:
    Count(median == M) = Count(median ≥ M) - Count(median > M)
    
We define a balance score:
    If A[i] ≥ M → we treat it as +1
    If A[i] < M → we treat it as -1

Convert the array into a running sum (prefix balance).
The subarrays that contribute to valid medians will have balanced prefix sums.
'''
class Solution:
    def solve(self, n, A, m):
        mp=[0]*(2*n+1)
        current=n
        total=0
        ans=0
        mp[current]+=1

        for i in range(n):
            if A[i]>=m:
                total+= mp[current]
                current+=1
            else:
                total-=mp[current-1]
                current-=1
            ans+=total
            mp[current] += 1
        return ans
        
    def countSubarray(self, N, A, M): 
        return self.solve(N,A,M)-self.solve(N,A,M+1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, M)
        print(ans)

        print("~")
# } Driver Code Ends