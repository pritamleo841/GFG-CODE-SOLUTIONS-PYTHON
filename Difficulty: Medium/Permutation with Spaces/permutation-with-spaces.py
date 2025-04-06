#User function Template for python3


class Solution:

    def permutation(self, s):
        res = []
        def backtrack(char,string):
            if len(string)==0:
                res.append(char)
                return
            val = string[0]
            backtrack(char+" "+val,string[1:]) #with space
            backtrack(char+val,string[1:]) #without space
        backtrack(s[0],s[1:])
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        S = input()
        ans = ob.permutation(S)
        write = ""
        for i in ans:
            write += "(" + i + ")"
        print(write)

        print("~")
# } Driver Code Ends