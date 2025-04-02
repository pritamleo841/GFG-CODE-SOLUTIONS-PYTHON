#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        res = []
        
        def isPalindrome(start,end):
            while start<=end:
                if S[start]!=S[end]:
                    return False
                start+=1
                end-=1
            return True
            
        def recur(index,path):
            if index==len(S):
                res.append(path[:])
                return
            for i in range(index,len(S)):
                if isPalindrome(index,i):
                    path.append(S[index:i+1])
                    recur(i+1,path)
                    path.pop()
            
        recur(0,[])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
        print("~")
# } Driver Code Ends