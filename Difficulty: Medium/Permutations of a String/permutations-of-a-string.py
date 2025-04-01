#User function Template for python3

class Solution:
    def findPermutation(self, s):
        res = set()
        s=list(s)
        def permute(low,high):
            if low==high:
                res.add("".join(s))
                return
            for i in range(low,high):
                s[low],s[i]=s[i],s[low]
                permute(low+1,high)
                s[low],s[i]=s[i],s[low]
        permute(0,len(s))
        return list(res)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends