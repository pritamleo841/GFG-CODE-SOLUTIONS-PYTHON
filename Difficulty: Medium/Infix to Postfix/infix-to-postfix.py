class Solution:
    def precedence(self,op):
        if op=='^':
            return 3
        elif op in '*/':
            return 2
        elif op in '+-':
            return 1
        return 0
    def InfixtoPostfix(self, s):
        #Shunting Yard Algorithm
        '''
        1.If the character is an operand → add it to the output.
        2.If the character is an open parenthesis '(' → push to stack.
        3.If the character is a closing parenthesis ')' → pop from stack to output until '(' is found.
        4.If the character is an operator →
            4a.While the top of the stack has higher or equal precedence, pop from stack to output.
            4b.Push the current operator to the stack.
        5.After reading the whole expression → pop any remaining operators in the stack to output.
        '''
        stack=[]
        output=[]
        for ch in s:
            if ch.isalnum():
                output.append(ch)
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                while stack and stack[-1]!='(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack 
                    and stack[-1]!='(' 
                    and self.precedence(stack[-1])>=self.precedence(ch)):
                        output.append(stack.pop())
                stack.append(ch)
        while stack:
            output.append(stack.pop())
        return ''.join(output)
        
                
                
                
                
                