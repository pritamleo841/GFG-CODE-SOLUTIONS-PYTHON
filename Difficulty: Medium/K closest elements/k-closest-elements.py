#User function Template for python3

class Solution:
    def binarySearch(self,arr,low,high,key):
        if arr[high] <= x:
            return high
        if arr[low] >= x:
            return low

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= x and (mid == len(arr) - 1 or arr[mid + 1] > x):
                return mid
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1  # Fallback case (should not occur with proper input)

        
    def printKClosest(self, arr, n, k, x):
        # code here
        ans = []
        index = self.binarySearch(arr,0,n-1,x)
        #Using two pointers to look for closest elements
        left,right = float('-inf'),float('inf')
        
        if arr[index]==x: #not considering x in arr
            left=index-1
        else:
            left=index
            
        right=index+1
        
        while k>0 and left>=0 and right<n:
            x1=x-arr[left]
            x2=arr[right]-x
            #take whichever has the lowest difference(i.e., closest)
            if x1<x2:
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
            k-=1
        
        #take remaining elements from sides if k is not 0
        while k>0 and left>=0:
            ans.append(arr[left])
            left-=1
            k-=1
        
        while k>0 and right<n:
            ans.append(arr[right])
            right+=1
            k-=1
        
        return ans
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

        print("~")
# } Driver Code Ends