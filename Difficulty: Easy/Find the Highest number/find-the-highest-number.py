#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		low,high=0,len(a)-1
        
        while low<=high:
            mid=low+(high-low)//2
            # Check if mid is a peak
            if(mid == 0 or a[mid]>a[mid-1]) and (mid==len(a)-1 or a[mid]>a[mid+1]):
                return a[mid]
            # Move to the side with the higher value
            if mid<len(a)-1 and a[mid]<a[mid+1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

        print("~")
# } Driver Code Ends