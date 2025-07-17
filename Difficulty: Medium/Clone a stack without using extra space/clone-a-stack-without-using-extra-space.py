#User function Template for python3

class Solution:
    def clonestack(self, st, cloned):
        '''
        1.Pop the top of st.
        2.Recurse until the stack is empty.
        3.While unwinding the recursion:
            3a.Push the element back to original st.
            3b.Also push into cloned.
        '''
        if not st:
            return
        top=st.pop()
        self.clonestack(st,cloned)
        st.append(top)
        cloned.append(top)
        