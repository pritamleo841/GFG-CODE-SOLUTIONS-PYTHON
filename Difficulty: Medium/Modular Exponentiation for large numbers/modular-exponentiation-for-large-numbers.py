#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		ans=1
		k=n
		while n>0:
		    if n%2==1:
		        ans=(ans%m)*(x%m)
		        n-=1
		    else:
		        n=n/2
		        x=(x%m)*(x%m)
		if k<0:
		    return (1/(ans%m))%m
		else:
		    return ans%m
		  


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        x, n, m = input().split()
        x = int(x)
        n = int(n)
        m = int(m)

        ob = Solution()
        ans = ob.PowMod(x, n, m)
        print(ans)

        print("~")

# } Driver Code Ends