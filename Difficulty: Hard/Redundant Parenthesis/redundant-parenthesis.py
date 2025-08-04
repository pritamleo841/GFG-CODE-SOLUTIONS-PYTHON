#User function Template for python3

class Solution:
    def removeBrackets (self, s):
        # Final result string
        ans = ""
    
        # Flag variable (unused here, might be for extended logic)
        f = 0
    
        # v[i] = index of the opening bracket for closing or current char at index i
        v = [0] * len(s)
    
        # Stack to manage bracket indices
        st = []
    
        # st1 stores indices of sub-expressions with '+' or '-' inside brackets
        # st2 stores the indices of brackets that must be preserved (not redundant)
        # st3 stores indices of sub-expressions with '*' or '/' inside brackets
        st1, st2, st3 = set(), set(), set()
    
        # First pass: determine the bracket ownership and record operators
        for i in range(len(s)):
            if s[i] == '(':
                # Opening bracket: push to stack
                st.append(i)
                v[i] = st[-1]
            elif s[i] == ')':
                # Closing bracket: match it with the last opening bracket
                v[i] = st[-1]
                st.pop()
            elif s[i] == '+' or s[i] == '-':
                if len(st) > 0:
                    # Mark the outermost bracket of this '+' or '-' expression
                    v[i] = st[-1]
                    st1.add(st[-1])
            elif s[i] == '*' or s[i] == '/':
                if len(st) > 0:
                    # Mark the outermost bracket of this '*' or '/' expression
                    v[i] = st[-1]
                    st3.add(st[-1])
            elif len(st) > 0:
                # For other characters inside brackets, record which bracket group they belong to
                v[i] = st[-1]
    
        # Second pass: determine which brackets must be kept (not redundant)
        for i in range(len(s)):
            if s[i] not in "*-/":
                # We only care about '*', '/', and '-' for precedence-sensitive contexts
                continue
    
            j = i + 1
            if s[i] == '-':
                # If there's a '-' followed by nested brackets, and those brackets
                # contain '+' or '-' inside, they must be preserved.
                while j < len(s) and s[j] == '(':
                    if v[j] in st1:
                        st2.add(j)  # mark for preservation
                    j += 1
                continue
    
            # For '+' and '*', if next brackets contain '+' or '-', mark them
            j = i + 1
            while j < len(s) and s[j] == '(':
                if v[j] in st1:
                    st2.add(j)
                j += 1
    
            # Special check for '/' followed by brackets containing '* or /'
            if s[i] == '/':
                j = i + 1
                while j < len(s) and s[j] == '(':
                    if v[j] in st3:
                        st2.add(j)
                    j += 1
    
            # Now check on the left side for redundant ')'s before this operator
            j = i - 1
            while j >= 0 and s[j] == ')':
                if v[j] in st1:
                    st2.add(j)
                j -= 1
    
        # Final pass: rebuild the result by skipping unnecessary parentheses
        for i in range(len(s)):
            if s[i] != ')' and s[i] != '(':
                ans += s[i]  # keep all non-parenthesis characters
            else:
                if v[i] in st2:
                    ans += s[i]  # keep only necessary '(' and ')'
    
        return ans