#User function Template for python3

#User function Template for python3
class Solution:
	def nthRowOfPascalTriangle(self,n):
        #C(n,k)=C(n,k−1)× (n−k+1)//k
        arr=[1]
        def recur(n,k):
            if k==0:
                return 1
            val=recur(n,k-1)*(n-k+1)//k
            arr.append(val)
            return val
        recur(n-1,n-1) #converted to 0-based indexing
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends