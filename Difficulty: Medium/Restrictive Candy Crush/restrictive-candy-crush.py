#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        '''
        We traverse the string once and use a stack of pairs:
        Each element in the stack is (character, count) representing consecutive characters.
        If the current character is the same as the one on top of the stack, increment the count.
        If the count becomes equal to k, pop it from the stack (i.e., remove the group).
        If it's a new character, push (char, 1).
        At the end, reconstruct the string from the stack.
        '''
        if k==1:
            return ""
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])
        return ''.join(ch*count for ch,count in stack)
