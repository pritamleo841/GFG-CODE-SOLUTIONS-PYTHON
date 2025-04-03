
class Solution:
    def decodedString(self, s):
        '''
        1.Traverse the string character by character.
        2.If a digit is encountered (3[b2[ca]] → 3), parse the number (which can be multiple digits like 23).
        3.If [ is encountered, push the current string and repeat count onto the stack and reset temporary variables.
        4.If ] is encountered, pop from the stack, repeat the substring, and append it to the previous string.
        5.If it's a letter, accumulate it in a temporary string.
        '''
        stack = [] #<previous_string,repeat_count>
        curr_str = ""
        curr_num = 0
        for char in s:
            if char.isdigit():
                curr_num=curr_num*10+int(char)
            elif char=='[':
                stack.append((curr_str,curr_num))
                curr_str=""
                curr_num=0
            elif char=="]":
                prev_str,repeat_count = stack.pop()
                curr_str = prev_str+(curr_str*repeat_count)
            else:
                curr_str+=char
        return curr_str

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends