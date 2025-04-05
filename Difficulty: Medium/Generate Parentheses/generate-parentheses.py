#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        '''
        Only add open parenthesis if open<n
        Only add close parenthesis if close<open
        stop when open=close=n
        
        '''
        res = []
        ans = []
        def backtrack(openN,closeN):
            if openN==closeN==n:
                res.append("".join(ans))
                return
            if openN<n:
                ans.append("(")
                backtrack(openN+1,closeN)
                ans.pop()
            if closeN<openN:
                ans.append(")")
                backtrack(openN,closeN+1)
                ans.pop()
        backtrack(0,0)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

        print("~")
# } Driver Code Ends