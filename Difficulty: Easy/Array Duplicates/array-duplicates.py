from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        freq=Counter(arr)
        return [num for num,count in freq.items() if count>1]