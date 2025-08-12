# Function should return an integer value
class Solution:
    def convertFive(self, n):
        lst=list(str(n))
        for i in range(len(lst)):
            if lst[i]=='0':
                lst[i]='5'
        return int(''.join(lst))