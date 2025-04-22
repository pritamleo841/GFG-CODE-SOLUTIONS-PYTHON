#User function Template for python3

class Solution:
    def reverseString(self, s):
        st = list(reversed(s))
        res=[]
        unique=set()
        for ch in st:
            if ch not in unique and ord(ch)!=32:
                res.append(ch)
                unique.add(ch)
        return "".join(res)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverseString(s)
        print(ans)
        print("~")
# } Driver Code Ends