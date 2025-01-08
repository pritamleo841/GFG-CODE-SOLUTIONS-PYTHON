#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
        low,high=0,len(arr)-1
        
        while low<=high:
            mid = low + (high - low) // 2
            # Check if mid is a peak
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return arr[mid]
            # Move to the side with the higher value
            if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends