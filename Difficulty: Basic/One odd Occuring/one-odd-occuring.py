class Solution:
    def getOddOccurrence(self, arr):
        res=0
        for elem in arr:
            res^=elem
        return res