
class Solution:
    def maxDays(self, arr):
        max_day=0
        for elem in arr:
            max_day=max(max_day,elem)
        return max_day