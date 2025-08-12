# Function should return an integer value
class Solution:
    def convertFive(self, n):
        if n==0:
            return 5
            
        place=1
        res=0
        while n:
            rem=n%10
            if rem==0:
                rem=5
            res+=place*rem
            place*=10
            n//=10
        return res
        '''
        lst=list(str(n))
        for i in range(len(lst)):
            if lst[i]=='0':
                lst[i]='5'
        return int(''.join(lst))
        '''