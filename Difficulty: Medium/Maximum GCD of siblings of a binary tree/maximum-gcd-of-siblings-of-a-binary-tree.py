#User function Template for python3

class Solution:
    def maxBinTreeGCD(self, arr, N):
        # code here 
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
            
        if N==1 or N==2:
            return 0
        arr.sort(key = lambda x:(x[0],x[1]))
        max_gcd = 0
        for i in range(len(arr)-1):
            if arr[i][0]==arr[i+1][0]:
                max_gcd = max(max_gcd,gcd(arr[i][1],arr[i+1][1]))
        return max_gcd



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from math import gcd
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        
        for i in range(N-1):
            u,v=map(int,input().split())
            arr.append([u,v])
        
        ob = Solution()
        print(ob.maxBinTreeGCD(arr,N))
        print("~")
# } Driver Code Ends