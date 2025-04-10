#User function Template for python3

class Solution:
    def permutation(self,s):
        res = []
        def permute(l,r,s):
            if l==r:
                res.append("".join(s))
            else:
                for i in range(l,r+1):
                    s[l],s[i]=s[i],s[l]
                    permute(l+1,r,s)
                    s[l],s[i]=s[i],s[l]
        permute(0,len(s)-1,list(s))
        return sorted(res)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
        print("~")
# } Driver Code Ends