#User function Template for python3

class Solution:
    def solve (self, X, Y, S):
        #greedy+stack-based approach 
        def remove_pattern(s,first,second,value):
            stack=[]
            count=0
            for ch in s:
                #If top of stack is 'first' and current char is 'second', we found a match
                if stack and stack[-1]==first and ch==second:
                    stack.pop()
                    count+=1
                else:
                    stack.append(ch)
            #Return the resulting string after removals and total value count
            return ''.join(stack),count*value
        '''
        Prioritize the higher-valued pair first:
            -If X>Y,remove "pr" first,then "rp".
            -If Y>X,remove "rp" first,then "pr".
        '''
        if X>=Y:
            #Remove "pr" first
            S,val1=remove_pattern(S,'p','r',X)
            S,val2=remove_pattern(S,'r','p',Y)
        else:
            #Remove "rp" first
            S,val1=remove_pattern(S,'r','p',Y)
            S,val2=remove_pattern(S,'p','r',X)

        return val1+val2
            