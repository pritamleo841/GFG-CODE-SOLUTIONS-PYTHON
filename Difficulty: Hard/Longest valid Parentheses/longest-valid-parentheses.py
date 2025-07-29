
class Solution:
    def maxLength(self, s):
        '''
        Step 1: Initialize Stack
            Push -1 initially as a base for calculating lengths when a valid substring starts at index 0.

        Step 2: Iterate Through the String
            For each character:
                If '(', push its index to the stack.
                If ')':
                    Pop the top index (which would ideally be a '(' match).
            If the stack becomes empty, push current index (i) as the new base (because no matching ( before this )).
            If the stack is not empty, calculate the length:    current length = i - stack[-1]
        This works because the index at the new top of stack is the start of the last unmatched part.
        Step 3: Keep Track of Maximum Length
            Update a max_len variable each time you find a longer valid substring.
        '''
        stack=[-1]
        max_len=0
        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len=max(max_len,i-stack[-1])
                else:
                    stack.append(i)
        return max_len
        