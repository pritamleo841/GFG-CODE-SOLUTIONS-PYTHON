#User function Template for python3

class Solution:
    def findMaxLen(ob, s):
        #SC-O(1), TC-O(N)
        #Longest Valid Parentheses Problem Variant
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