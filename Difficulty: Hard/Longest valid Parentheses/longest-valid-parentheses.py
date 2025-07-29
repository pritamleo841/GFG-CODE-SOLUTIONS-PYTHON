
class Solution:
    def maxLength(self, s):
        '''
        In Stack based approach,You don’t actually care about the exact positions of matching brackets — just the number of valid pairs.
        That insight leads to a counter-based solution — where instead of remembering positions,
        you count how many '(' and ')' you've seen.
        
        Left-to-Right Scan:
            1.Use left and right counters.
            2.If left == right, you’ve found a valid substring: length = 2 * right.
            3.If right > left, reset both counters (invalid substring).

        Right-to-Left Scan:
            1.Same as above, but reversed.
            2.This handles cases like "(()" where extra '(' at the start could be ignored only if we scan from the end.
        '''
        #SC-O(1), TC-O(N)
        left=right=max_len=0
        # Left to Right pass
        for ch in s:
            if ch=='(':
                left+=1
            else:
                right+=1
            if left==right:
                max_len=max(max_len, 2 * right)
            elif right>left:
                left=right=0  # reset
    
        # Right to Left pass
        left=right=0
        for ch in reversed(s):
            if ch=='(':
                left+=1
            else:
                right+=1
            if left==right:
                max_len=max(max_len, 2 * left)
            elif left>right:
                left=right=0  # reset
    
        return max_len
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
        
        #O(n)->TC,SC
        
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
        '''
        