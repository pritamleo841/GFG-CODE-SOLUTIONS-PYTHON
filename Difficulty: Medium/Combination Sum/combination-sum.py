#User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, target):
        ans = []
        arr.sort()
        def backtrack(curr,curr_sum,index):
            if curr_sum==target:
                ans.append(curr[:])
                return
            for i in range(index,len(arr)):
                if curr_sum+arr[i]>target:
                    return
                curr.append(arr[i]) #pick it
                backtrack(curr,curr_sum+arr[i],i)
                curr.pop() #don't pick
        backtrack([],0,0)
        return ans
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        ans = ob.combinationSum(arr, sum)
        if (len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                ans[i].sort()
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()
        print("~")

# } Driver Code Ends