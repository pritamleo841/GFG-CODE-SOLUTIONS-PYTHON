
class Solution:
    def isBalanced(self,s):
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or stack.pop()!=bracket_map[ch]:
                    return False
        return len(stack) == 0