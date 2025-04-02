#Your Function should return a list containing all possible IP address

class Solution:
    def generateIp(self, s):
        res = []
        if len(s)>12:
            return []
        def backtrack(index,dots,curIP):
            if dots==4 and index==len(s):
                res.append(curIP[:-1])#exclude last dot
                return
            if dots>4:
                return
            for i in range(index,min(index+3,len(s))):
                segment=s[index:i+1]
                if int(segment)>255:  # Check valid range
                    continue
                if s[index]=="0" and i>index:  # Skip leading zeros
                    continue
                backtrack(i+1,dots+1,curIP+segment+".")
        backtrack(0,0,"")
        return res


#{ 
 # Driver Code Starts
#Main
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().generateIp(s)
        res.sort()
        if (len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
        print("~")

# } Driver Code Ends