#User function Template for python3

class Solution:

    def fun(self, s):
        distinct=set()
        for i in range(len(s)):
            if i<len(s)-1:
                distinct.add(s[i]+s[i+1])
        return len(distinct)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.fun(s))
# } Driver Code Ends