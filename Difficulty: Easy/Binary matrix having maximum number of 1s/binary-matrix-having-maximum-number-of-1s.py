#User function Template for python3

class Solution:
    def binarySearch(self,arr,key=1):
        low=0
        high=len(arr)-1
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==key:
                ans=mid
                high=mid-1
            elif arr[mid]>key:
                high=mid-1
            else:
                low=mid+1
        return ans
        
    def findMaxRow(self, mat, N):
        # Code here
        maxOnes=-1
        rowIdx=-1
        for i,row in enumerate(mat):
            indexOfFirstOne = self.binarySearch(row)
            if indexOfFirstOne!=-1:
                numOnes = len(row)-indexOfFirstOne
                if numOnes > maxOnes:
                    maxOnes = numOnes
                    rowIdx = i
        if rowIdx==-1 and maxOnes==-1:
            return 0,0
        return rowIdx, maxOnes


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
        print("~")
# } Driver Code Ends