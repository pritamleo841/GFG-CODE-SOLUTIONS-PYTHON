#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        low = self.leftBSearch(arr,x)
        high = self.rightBSearch(arr,x)
        if low==-1 and high==-1:
            return [-1]
        else:
            return [low,high]
        
    def leftBSearch(self,v,x):
        result=-1
        low,high=0,len(v)-1
        while low<=high :
            mid=low+(high-low)//2
            if v[mid]==x:
                result=mid
                high=mid-1
            elif v[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return result
        
    def rightBSearch(self,v,x):
        result=-1
        low,high=0,len(v)-1
        while low<=high :
            mid=low+(high-low)//2
            if v[mid]==x:
                result=mid
                low=mid+1
            elif v[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        ans = ob.firstAndLast(x, arr)
        s = (" ").join(map(str, ans))
        print(s)
        print("~")

# } Driver Code Ends