#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        ans = []
        contact = sorted(set(contact))  # remove duplicates and sort once
        for i in range(1,len(s)+1):
            prefix = s[:i]
            unique = set()
            for c in contact:
                if c.startswith(prefix):
                    unique.add(c)
            if not unique:
                temp = ["0"]
            else:
                temp = sorted(unique)
            ans.append(temp)
        return ans
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
        print("~")
# } Driver Code Ends