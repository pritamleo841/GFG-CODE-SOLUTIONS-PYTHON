#User function Template for python3

class Solution:
    def farNumber(self,N,Arr):
        #code here
        #Find suffix array and store min elements
        suffix = [0]*N
        suffix[N-1]=Arr[N-1]
        for i in range(N-2,-1,-1):
            suffix[i]=min(suffix[i+1],Arr[i])
        ans= [-1]*N
        #for each element in arr, find suffix min from suffix array
        for i in range(N):
            low=i+1
            high=N-1
            while low<=high:
                mid=low+(high-low)//2
                # If current element in the suffix
                # is less than a[i] then move right
                if suffix[mid]<Arr[i]:
                    ans[i]=mid
                    low=mid+1
                else:
                    high=mid-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        N=int(input())
        Arr=[int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.farNumber(N,Arr)
        
        for i in ans:
            print(i,end=" ")
        print()
        print("~")
# } Driver Code Ends