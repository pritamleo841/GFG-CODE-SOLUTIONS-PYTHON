#User function Template for python3
from functools import lru_cache
class Solution:
    def count(self, N):
        '''
        The number of valid handshake pairings for N = 2n is given by the Nth Catalan number:
        Cn= (2n)!//(n!×(n+1)!) where: n = N/2 (since N is even)
        or Catalan Number => C(2n,n)//(n+1)
        '''
        @lru_cache(None)  # Memoize previously computed results
        def combination(n,r): # Recurrence relation [nCr]
            return 1 if (r==0 or r==n) else combination(n-1,r-1)+combination(n-1,r)
        n=N//2
        return combination(2*n,n)//(n+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))
        print("~")
# } Driver Code Ends