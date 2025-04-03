#User function Template for python3

class Solution:
	def UniquePartitions(self, n):
		res = []
		def recur(part,part_sum,max_val):
		    if part_sum==n:
		        res.append(part[:])
		        return
		    for i in range(max_val,0,-1): #Start from max_val to ensure non-increasing order
		        if part_sum+i<=n:
		            part.append(i)
		            recur(part,part_sum+i,i) #Pass i as the new max_val
		            part.pop()
		recur([],0,n)
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end = " ")
		print()

# } Driver Code Ends