# your task is to complete this function
# function should return True/False or 1/0
# pat: pattern
# txt: text
class Solution:
    def wildCard(self,txt, pat):
        '''
        Let dp[i][j] be true if the first i characters of the pattern 
        match the first j characters of the text.
        Base Cases:
            dp[0][0] = true → Empty pattern matches empty text.
            dp[i][0] = true only if pat[0..i-1] are all '*'
            dp[0][j] = false for all j > 0 → empty pattern can't match non-empty text.
        DP Formula:
            If pat[i-1] == txt[j-1] or pat[i-1] == '?', then dp[i][j] = dp[i-1][j-1]
            If pat[i-1] == '*', then:
            dp[i][j] = dp[i-1][j] (treat * as empty)
            or dp[i][j] = dp[i][j-1] (treat * as matching one or more characters)
        '''
        m,n=len(pat),len(txt)
        dp=[[False]*(n+1) for _ in range(m+1)]
        #Empty pattern matches empty text
        dp[0][0]=True
        #Initialize first column(pattern vs empty text)
        for i in range(1,m+1):
            if pat[i-1]=='*':
                dp[i][0]=dp[i-1][0]
            else:
                break
        for i in range(1,m+1):
            for j in range(1,n+1):
                if pat[i-1]==txt[j-1] or pat[i-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif pat[i-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
        return dp[m][n]
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(string, pattern):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends