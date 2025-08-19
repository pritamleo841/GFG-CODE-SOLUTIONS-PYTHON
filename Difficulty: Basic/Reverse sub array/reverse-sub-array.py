#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		arr[l-1:r] = arr[l-1:r][::-1]
        return arr