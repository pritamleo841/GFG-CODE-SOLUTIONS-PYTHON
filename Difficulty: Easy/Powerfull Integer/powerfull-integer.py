from typing import List
from collections import defaultdict
class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        mp = {}
        # Iterating over all the intervals
        # and updating the count in the dictionary
        for x in intervals:
            mp[x[0]] = mp.get(x[0], 0) + 1
            mp[x[1] + 1] = mp.get(x[1] + 1, 0) - 1
        ans = -1
        temp = 0
        # Iterating over the dictionary to find
        # the kth power of an integer
        for key in sorted(mp.keys()):
            value = mp[key]
            # If the count in the dictionary
            # is positive
            if value >= 0:
                temp += value
                # Checking if the count
                # is greater than or
                # equal to k
                if temp >= k:
                    ans = key
            # If the count in the dictionary
            # is negative
            else:
                # Checking if the previous
                # count was greater
                # than or equal to k
                if temp >= k:
                    ans = key - 1
                temp += value
    
        # Returning the kth power
        # of an integer
        return ans
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

        print("~")
# } Driver Code Ends