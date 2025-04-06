
from typing import List


class Solution:
    def increasingNumbers(self, n : int) -> List[int]:
        res = []
        # Special case for n == 1: include 0
        if n==1:
            return [i for i in range(10)]
        def generate(path,start):
            if len(path)==n:
                res.append(int("".join(map(str,path))))
                return
            for i in range(start,10):
                path.append(i)
                generate(path,i+1)
                path.pop()
        for i in range(1,10):
            generate([i],i+1)
        return res



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

        n = int(input())

        obj = Solution()
        res = obj.increasingNumbers(n)

        IntArray().Print(res)

        print("~")
# } Driver Code Ends