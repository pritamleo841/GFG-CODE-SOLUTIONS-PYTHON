#User function Template for python3
from collections import defaultdict
class Solution:
	def TotalPairs(self, nums, k):
	    '''
	    So for every num, you're checking:
        🔹 1. num + k in seen
        This checks if (num, num + k) exists in the array.
        If num + k is already in seen, then (num, num + k) is a valid pair because:
            num - (num + k) = -k → absolute difference is k.

        🔹 2. num - k in seen
        This checks if (num - k, num) is a valid pair.
            Because num - (num - k) = k.
        👉 You check both directions to cover all valid unordered pairs.
	    '''
		pairs=set()
		seen=set()
		for num in nums:
		    if k==0:
		        if num in seen:
		            pairs.add((num,num))
	        else:
	            if num+k in seen:
	                pairs.add((num,num+k))
	            if num-k in seen:
	                pairs.add((num-k,num))
		    seen.add(num)
		return len(pairs)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.TotalPairs(nums, k)
		print(ans)
# } Driver Code Ends