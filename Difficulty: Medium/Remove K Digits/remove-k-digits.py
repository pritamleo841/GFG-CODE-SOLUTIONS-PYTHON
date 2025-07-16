class Solution:
    def removeKdigits(self, s, k):
        #stack+greedy
        '''
        To get the smallest number,we want to remove digits from left to right such that:
            1.If a digit is greater than the next digit, it's a good candidate to remove.
            2.We maintain a monotonic increasing stack (digits should increase from left to right).
            3.After traversing the digits:
                3a.If k > 0, we remove the last k digits from the end (in case the number was already increasing).
            4.Remove leading zeros in the result.
        '''
        stack=[]
        for digit in s:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        
        while k>0 and stack:
            stack.pop()
            k-=1
        
        result=''.join(stack).lstrip('0')
        return result if result else "0"