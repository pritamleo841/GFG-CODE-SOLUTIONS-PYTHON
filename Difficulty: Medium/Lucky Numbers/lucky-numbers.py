#User function Template for python3

class Solution:
    def isLucky(self, n,k=2): 
        #RETURN True OR False
        '''
        1.At step k, numbers are eliminated at intervals of k.
        2.If N is the k-th number in the remaining list, it is removed.
        3.We check recursively by reducing N accordingly.
        
        So, N is lucky if isLucky(N−N//k,k+1) is True
        '''
        if n<k:
            return True
        if n%k==0:
            return False
        return self.isLucky(n-n//k,k+1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
        print("~")
# } Driver Code Ends