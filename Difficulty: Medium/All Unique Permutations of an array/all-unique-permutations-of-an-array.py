#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        res = []
        arr.sort()
        visited=set()
        def backtrack(path):
            if len(arr)==len(path):
                res.append(path[:])
                return
            for i in range(len(arr)):
                if i in visited:
                    continue
                if i>0 and arr[i]==arr[i-1] and (i-1) not in visited:
                    continue
                visited.add(i)
                path.append(arr[i])
                backtrack(path)
                path.pop()
                visited.remove(i)
        backtrack([])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
        print("~")
# } Driver Code Ends