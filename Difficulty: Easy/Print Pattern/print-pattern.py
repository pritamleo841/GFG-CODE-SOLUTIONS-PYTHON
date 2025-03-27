#User function Template for python3

class Solution:
    def pattern(self, N):
        arr = []
        def recur(n):
            arr.append(n) #insert while going down in the recursion
            if n<=0:
                return
            recur(n-5)
            arr.append(n) #insert while going up in the recursion
        recur(N)
        return arr
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends