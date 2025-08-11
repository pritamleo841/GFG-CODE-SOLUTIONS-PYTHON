#User function Template for python3



class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        def isValid(num):
            # Must have at least 2 digits
            if num < 10:
                return False
            digits = list(map(int, str(num)))
            for i in range(1, len(digits)):
                if abs(digits[i] - digits[i-1]) != 1:
                    return False
            return True
        
        res = []
        for num in arr:
            if num < k and isValid(num):
                res.append(num)
        return res