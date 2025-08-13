#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
		# two-pointer+in-sort approach
		n=len(arr)
		left,right=0,n-1
		while left<right:
		    #Move left pointer if current element is even
		    if arr[left]%2==0:
		        left+=1
		    #Move right pointer if current element is odd
		    elif arr[right]%2!=0:
		        right-=1
		    else:
		        #Move right pointer if current element is even
		        #Move left pointer if current element is odd
		        arr[left],arr[right]=arr[right],arr[left]
		        left+=1
		        right-=1
		 
		i=0
		while i<n and arr[i]%2==0:
		    i+=1
		arr[:i]=sorted(arr[:i])
		arr[i:]=sorted(arr[i:])
		return arr