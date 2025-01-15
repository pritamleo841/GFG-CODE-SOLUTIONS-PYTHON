#User function Template for python3
class Solution:
    def lowerBound(self,a,key):
        low,high=0,len(a)-1
        ans=len(a)
        while low<=high :
            mid = low+(high-low)//2
            if a[mid]>=key:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
	def constructLowerArray(self,arr):
		# code here
		n=len(arr)
		ans = [] #to store answers
		temp = [] #to store elements in reverse order of arr dynamically
		for i in range(n-1,-1,-1):
		    index = self.lowerBound(temp,arr[i])
		    ans.append(index);
		    temp.insert(index,arr[i])
		return ans[::-1]
		    
		        
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

        print("~")

# } Driver Code Ends