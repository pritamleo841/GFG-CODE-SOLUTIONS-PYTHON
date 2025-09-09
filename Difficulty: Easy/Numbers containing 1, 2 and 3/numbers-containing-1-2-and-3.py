class Solution:
    def filterByDigits(self, arr):
        #code here
        res=[]
        for elem in arr:
            if all(digit in ['1','2','3'] for digit in str(elem)):
                res.append(elem)
        return res if len(res)>0 else [-1]
                
        