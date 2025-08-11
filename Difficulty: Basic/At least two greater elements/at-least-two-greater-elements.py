#User function Template for python3

class Solution:
    def findElements(self,arr):
        n=len(arr)
        if n<=2:
            return []
        arr.sort()
        arr.pop()
        arr.pop()
        return arr
    
