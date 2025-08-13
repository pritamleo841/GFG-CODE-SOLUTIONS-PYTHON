#User function Template for python3

class Solution:
	def common_digits(self, nums):
		distinct=set()
		for elem in nums:
		    n=elem
		    while n>0:
		        distinct.add(n%10)
		        n//=10
		return sorted(list(distinct))
		        