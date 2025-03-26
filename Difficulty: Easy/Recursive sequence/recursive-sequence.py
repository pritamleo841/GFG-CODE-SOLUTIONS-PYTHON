#User function Template for python3

class Solution:
    def product_series(self, start, count, mod=10**9+7):
        """Computes the product of 'count' consecutive numbers starting from 'start' under modulo."""
        if count==0:
            return 1
        return (start*self.product_series(start+1,count-1,mod))%mod

    def sequence(self, n, mod=10**9+7):
        """Computes F(n) recursively using the correct recurrence relation."""
        if n==1:
            return 1  # Base case
        
        start_n=1+((n-1)*n)//2  # Starting number for nth term
        return (self.sequence(n-1,mod)+self.product_series(start_n,n,mod))%mod
        '''
        #Iterative solution -
        
        total_sum=0
        start=1
        for k in range(1,n+1):
            product=1
            for i in range(start,start+k):
                product=product*i
            total_sum+=product
            start+=k
        return total_sum
        '''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
        print("~")
# } Driver Code Ends