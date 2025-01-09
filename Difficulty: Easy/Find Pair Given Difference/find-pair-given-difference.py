
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # Handle the case where the list has fewer than 2 elements
        if len(arr) < 2:
            return False
        arr=sorted(arr)
        i, j = 0, 1
        while j < len(arr):
            diff = arr[j] - arr[i]
            
            if i != j and diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1
            
            # Ensure j is always greater than i
            if i == j:
                j += 1
                
        return False


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        x = int(input())

        obj = Solution()
        res = obj.findPair(arr, x)

        print("true" if res else "false")
        print("~")

# } Driver Code Ends