class Solution:
    def maxLen(ob, s):
        stack=[-1]  # Initialize with base
        max_len=0
    
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len=max(max_len,i-stack[-1])
                else:
                    stack.append(i)  # Reset base
        return max_len