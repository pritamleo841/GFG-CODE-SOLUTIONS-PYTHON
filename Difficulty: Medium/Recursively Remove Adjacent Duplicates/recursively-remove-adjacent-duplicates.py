#User function Template for python3

class Solution:
    def removeUtil (self, S):
         def removeRedundant(s):
             newString = ""
		     i=0
		     while i<len(s):
		        if i<len(s)-1 and s[i]==s[i+1]:
		            while i<len(s)-1 and s[i]==s[i+1]:
		                i+=1
		        else:
		            newString+=s[i]
		        i+=1
		     return newString
		    
		 def helper(s,prev_length):
		    if len(s)==prev_length:
		        return s
		    newString = removeRedundant(s)
		    return helper(newString,len(s))
		    
		 return helper(S,-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        s = ob.removeUtil(S)
        if len(s) == 0:
            print("\"\"")
        else:
            print(s)

        print("~")

# } Driver Code Ends